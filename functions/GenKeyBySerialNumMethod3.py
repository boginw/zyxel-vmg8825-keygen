from common.doubleHash import doubleHash
from common.config import *
from common.mod3KeyGenerator import mod3KeyGenerator
from common.utils import *

keyStr1 = asAscii("IO")
keyStr2 = asAscii("lo")
keyStr3 = asAscii("10")

valStr = asAscii("23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789ABCDEF")

offset1 = 0x8 
offset2 = 0x20

def zcfgBeCommonGenKeyBySerialNumMethod3(serialNumber):
    round3 = doubleHash(serialNumber, 10)
    round3 = uppercaseBytearray(round3)

    dprint("uppercase: {}".format(asString(round3)))

    md5String = hashFunc(asAscii(serialNumber)).digest()

    strAsInt = (md5String[1] << 8) + md5String[2]

    dprint("strAsInt: {} - {}".format(strAsInt, format(strAsInt, "x")))
    
    (strAsInt, round4) = mod3KeyGenerator(strAsInt)
    
    dprint("round4: " + "".join([format(round4[i], "d") for i in range(10)]))

    for i in range(10):
        if (round4[i] == 1):
            newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('A')
            dprint("1: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr1[j]):
                    index = offset1 + ((strAsInt + j) % 0x18)
                    dprint("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break
        elif (round4[i] == 2):
            newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('a')
            dprint("2: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr2[j]):
                    index = offset2 + ((strAsInt + j) % 0x18)
                    dprint("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break
        else:
            newVal = (((round3[i] % 10) * 0x1000000) >> 0x18) + asChar('0')
            dprint("3: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr3[j]):
                    var = ((strAsInt + j) >> 0x1f) >> 0x1d
                    index = ((strAsInt + j + var) & 7) - var
                    dprint("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break

    return asString(round3[0:10])
