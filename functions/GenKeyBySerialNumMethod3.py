from doubleHash import doubleHash
from config import *
from binUtils import *

keyStr1 = asAscii("IO")
keyStr2 = asAscii("lo")
keyStr3 = asAscii("10")

valStr = asAscii("23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789ABCDEF")

offset1 = 0x8
offset2 = 0x20

def zcfgBeCommonGenKeyBySerialNumMethod3(serialNumber):
    round3 = doubleHash(serialNumber, 10)
    round3 = uppercaseBytearray(round3)

    #print("uppercase: {}".format(asString(round3)))

    md5String = hashFunc(asAscii(serialNumber)).digest()

    strAsInt = (md5String[1] << 8) + md5String[2]

    #print("strAsInt: {} - {}".format(strAsInt, format(strAsInt, "x")))
    
    round4 = [0] * 16

    found0s = 0
    found1s = 0
    found2s = 0

    while(found0s == 0 or found1s == 0 or found2s == 0):
        found0s = 0
        found1s = 0
        found2s = 0
        
        local_1e8 = 1
        strAsInt = strAsInt + 1

        for i in range(0, 10):            
            round4[i] = (strAsInt % (local_1e8 * 3)) // local_1e8
            
            if (round4[i] == 1):
                found1s = found1s + 1
            elif (round4[i] == 2):
                found2s = found2s + 1
            else:
                found0s = found0s + 1

            local_1e8 = local_1e8 << 1
    #print("round4: ", end="")
    #for i in range(10):
    #    print(format(round4[i], "d"), end="")
    #print()

    for i in range(10):
        if (round4[i] == 1):
            newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('A')
            #print("1: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr1[j]):
                    index = offset1 + ((strAsInt + j) % 18)
                    #print("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break
        elif (round4[i] == 2):
            newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('a')
            #print("2: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr2[j]):
                    index = offset2 + ((strAsInt + j) % 18)
                    #print("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break
        else:
            newVal = (((round3[i] % 10) * 0x1000000) >> 0x18) + asChar('0')
            #print("3: {} - {}".format(round3[i], format(newVal, "c")))
            round3[i] = newVal
            for j in range(2):
                if (round3[i] == keyStr3[j]):
                    var = ((strAsInt + j) >> 0x1f) >> 0x1d
                    index = ((strAsInt + j + var) & 7) - var
                    #print("=" + format(valStr[index], "c"))
                    round3[i] = valStr[index]
                    break
    output = bytearray(64)

    assignInt(output, 0, asInt(round3))
    assignInt(output, 4, asInt(round3, 4))
    output[8] = round3[8]
    output[9] = round3[9]
    return asString(output)
