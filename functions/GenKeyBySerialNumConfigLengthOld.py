from common.config import *
from common.utils import *

keyStr1 = asAscii("125680")
keyStr2 = asAscii("BDEFGILOQSZ")
keyStr3 = asAscii("acegilnoq")
keyStr4 = asAscii("120IOZoliz")
keyStr5 = asAscii("125690IOSZ")

valStr1 = asAscii("3479ACHJKMNPRTUVWXY")
valStr2 = asAscii("ACHJKMNPRTUVWXY")
valStr3 = asAscii("bdfhjkmprstuvwxyz")
valStr4 = asAscii("3456789ABCDEFGHJKLMNPQRTUXYSVW")
valStr5 = asAscii("3478ABCDEFGHJKLMNPQRTUVWXY")

def zcfgBeCommonGenKeyBySerialNumConfigLengthOld(
    serialNumber: str,
    inputKey: str or None,
    size: int,
    method: int = 1,
) -> str:
    if (inputKey == None or len(inputKey) == 0):
        return "1234"
    
    md5Result = hashFunc(asAscii(serialNumber)).digest()
    md5Result = hashFunc(asAscii("{}Account_Password{}".format(inputKey, md5Result))).digest()

    dprint("MD5: " + "".join([format(x, "x") for x in md5Result]))

    #strAsInt = (asInt(md5Result) >> 0x18) * 0x100 + (asInt(md5Result) >> 0x10 & 0xff)
    strAsInt = (md5Result[1] << 8) + md5Result[2]
    strAsInt = (md5Result[0] << 8) + md5Result[1]
    #strAsInt = 55000
    
    dprint("strAsInt: {} or 0x{}".format(strAsInt, format(strAsInt, "x")))

    methodMultiplier = 1

    if (method == 1): 
        methodMultiplier = 2
    elif (method == 2 or method == 3): 
        methodMultiplier = 3

    round1 = [0] * 16

    powerOf2 = 1
    for i in range(size):
        round1[i] = (strAsInt % (methodMultiplier * powerOf2)) // powerOf2
        powerOf2 = powerOf2 << 1

    numberOf1s = 0
    numberOf2s = 0
    numberOf3s = 0

    offset = 0
    round2 = bytearray(17)

    for i in range(size):
        char: str

        if (round1[i] == 1):
            char = format(md5Result[i] % 0x1a + asChar("A"), "c")
            numberOf1s = numberOf1s + 1
        elif (round1[i] == 2):
            char = format(md5Result[i] % 0x1a + asChar("a"), "c")
            numberOf2s = numberOf2s + 1
        else:
            md5Byte = md5Result[i]
            intermediate = (md5Byte * 0xcccccccd) >> 32 >> 3 << 1
            char = format(md5Byte - (((intermediate & 0xff) + ((intermediate << 2) & 0xff)) & 0xff) + asChar("0"), "c")
            numberOf3s = numberOf3s + 1

        round2[offset:offset + len(char)] = asAscii(char)
        offset = offset + len(char)

        dprint("round1[{}] == {}, len({}) = {}".format(i, round1[i], asString(round2), len(round2)))

        if (method == 2):
            for j in range(len(keyStr1)):
                if (round2[i] == keyStr1[j]):
                    intermediate = (strAsInt + j >> 0x1f) >> 0x1e
                    round2[i] = valStr1[(strAsInt + j + intermediate & 3) - intermediate]
                    break
            for j in range(len(keyStr2)):
                if (round2[i] == keyStr2[j]):
                    round2[i] = valStr2[(strAsInt + j) % 0xf]
                    break
            for j in range(len(keyStr3)):
                if (round2[i] == keyStr3[j]):
                    round2[i] = valStr3[(strAsInt + j) % 0x11]
                    break
        elif (method == 3):
            for j in range(len(keyStr4)):
                if (round2[i] == keyStr4[j]):
                    round2[i] = valStr4[(strAsInt + j) % 0x1e]
                    break
        else:
            for j in range(len(keyStr5)):
                if (round2[i] == keyStr5[j]):
                    round2[i] = valStr5[(strAsInt + j) % 0x1a]
                    break

    if (method == 2):
        zcfgBeCheckPasswordFormat(round2, strAsInt, numberOf1s, numberOf2s, numberOf3s)
    round2[size] = 0

    return asString(round2)

def zcfgBeCheckPasswordFormat(round2: bytearray, strAsInt: int, numberOf1s: int, numberOf2s: int, numberOf3s: int):
    if (numberOf1s == 0 or numberOf2s == 0 or numberOf3s == 0):
        round2[0] = valStr2[strAsInt % 0xf]
        round2[1] = valStr3[strAsInt % 0x11]
        intermediate = (strAsInt >> 0x1f) >> 0x1e
        round2[2] = valStr1[(strAsInt + intermediate & 3) - intermediate]
