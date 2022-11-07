from doubleHash import doubleHash
from config import *
from binUtils import *

strs5 = asAscii("125690IOSZ")
strs6 = asAscii("3478ABCDEFGHJKLMNPQRTUVWXY")

strs7 = asAscii("BDEFGILOQSZ")
strs8 = asAscii("acegilnoq")
strs9 = asAscii("125680")

strsA = asAscii("ACHJKMNPRTUVWXY")
strsB = asAscii("bdfhjkmprstuvwxyz")
strsC = asAscii("3479ACHJKMNPRTUVWXY")

def zcfgBeCommonGenKeyBySerialNumConfigLength(serialNumber, size, method=1):
    round3 = doubleHash(serialNumber, size)
    round3 = uppercaseBytearray(round3)

    md5String = hashFunc(asAscii(serialNumber)).digest()

    #strAsInt = (asInt(md5String, 0) >> 0x18) * 0x100 + ((asInt(md5String, 0) >> 0x10) & 0xff)
    strAsInt = (md5String[1] << 8) + md5String[2]

    if (method == 1):
        for i in range(0, size):
            for j in range(0, 10):
                if (round3[i] == strs5[j]):
                    round3[i] = strs6[(strAsInt + j) % 0x1a]
                    break
    elif(method == 2):
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
        
        for i in range(0, size):
            if (round4[i] == 1):
                newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('A')
                #print("1: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 0xb):
                    if (round3[i] == strs7[j]):
                        index = (strAsInt + j) % 0xf
                        round3[i] = strsA[index]
                        break
            elif (round4[i] == 2):
                newVal = (((round3[i] % 0x1a) * 0x1000000) >> 0x18) + asChar('a')
                #print("2: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 9):
                    if (round3[i] == strs8[j]):
                        index = (strAsInt + j) % 11
                        round3[i] = strsB[index]
                        break
            else:
                newVal = (((round3[i] % 10) * 0x1000000) >> 0x18) + asChar('0')
                #print("3: {} - {}".format(round3[i], format(newVal, "c")))
                round3[i] = newVal

                for j in range(0, 6):
                    if (round3[i] == strs9[j]):
                        var = (strAsInt + j >> 0x1f) >> 0x1e
                        index = ((strAsInt + j + var) & 3) - var
                        round3[i] = strsC[index]
                        break

    round3[size] = 0
    return asString(round3)
