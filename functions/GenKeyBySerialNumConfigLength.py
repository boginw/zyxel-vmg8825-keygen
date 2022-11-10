from common.config import *
from common.doubleHash import doubleHash
from common.mod3KeyGenerator import mod3KeyGenerator
from common.utils import *
from functions.IsApplyRandomAdminPasswordNewAlgorithm import *
from functions.GenKeyBySerialNumConfigLengthOld import *

keyStrMethod1 = asAscii("125690IOSZ")
valStrMethod1 = asAscii("3478ABCDEFGHJKLMNPQRTUVWXY")

keyStr1 = asAscii("BDEFGILOQSZ")
keyStr2 = asAscii("acegilnoq")
keyStr3 = asAscii("125680")

valStr1 = asAscii("ACHJKMNPRTUVWXY")
valStr2 = asAscii("bdfhjkmprstuvwxyz")
valStr3 = asAscii("3479") + valStr1

def zcfgBeCommonGenKeyBySerialNumConfigLength(
    serialNumber: str,
    inputKey: str or None,
    size: int,
    method: int = 1,
) -> str:
    if (not zcfgBeCommonIsApplyRandomAdminPasswordNewAlgorithm(serialNumber)):
        return zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serialNumber, inputKey, size, method)
    round3 = doubleHash(serialNumber, size)
    round3 = uppercaseBytearray(round3)

    md5String = hashFunc(asAscii(serialNumber)).digest()

    strAsInt = (md5String[0] << 8) + md5String[1]

    dprint("strAsInt: {} - {}".format(strAsInt, format(strAsInt, "x")))

    #strAsInt = 55000 # expected 12 / 0xc, 55000 / 0xd6d8

    ## (md5Result2[0] >> 0x10 & 0xff) * 0x100 + (md5Result2[0] >> 8 & 0xff)
    ## (md5Result2[0] >> 0x18) * 0x100 + (md5Result2[0] >> 0x10 & 0xff))

    dprint(asString(round3))

    if (method == 1):
        for i in range(0, size):
            for j in range(0, 10):
                if (round3[i] == keyStrMethod1[j]):
                    round3[i] = valStrMethod1[(strAsInt + j) % 0x1a]
                    break
    elif(method == 2):
        (strAsInt, round4) = mod3KeyGenerator(strAsInt)
    
        dprint("round4: ", end="")
        for i in range(10):
            dprint(format(round4[i], "d"), end="")
        dprint()
        
        for i in range(0, size):
            if (round4[i] == 1):
                newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('A')
                dprint("1: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 0xb):
                    if (round3[i] == keyStr1[j]):
                        index = (strAsInt + j) % 0xf
                        dprint("=" + format(valStr1[index], "c"))
                        round3[i] = valStr1[index]
                        break
            elif (round4[i] == 2):
                newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('a')
                dprint("2: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 9):
                    if (round3[i] == keyStr2[j]):
                        index = (strAsInt + j) % 11
                        dprint("=" + format(valStr2[index], "c"))
                        round3[i] = valStr2[index]
                        break
            else:
                newVal = (((round3[i] % 10) * 0x1000000) >> 0x18) + asChar('0')
                dprint("3: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 6):
                    if (round3[i] == keyStr3[j]):
                        var = (strAsInt + j >> 0x1f) >> 0x1e
                        index = ((strAsInt + j + var) & 3) - var
                        dprint("=" + format(valStr3[index], "c"))
                        round3[i] = valStr3[index]
                        break

    round3[size] = 0
    return asString(round3)
