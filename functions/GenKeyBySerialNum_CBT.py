from doubleHash import *
from config import *
from binUtils import *

strs1 = asAscii("120IOZoliz")
strs2 = asAscii("3456789ABCDEFGHJKLMNPQRTUXYSVW")

def zcfgBeCommonGenKeyBySerialNum_CBT(serialNumber):
    md5Result = hashFunc(asAscii("{}PSK_ra0".format(serialNumber))).digest()
    #strAsInt = (asInt(md5Result) >> 0x18) * 0x100 + (asInt(md5Result) >> 0x10 & 0xff)
    strAsInt = (md5Result[1] << 8) + md5Result[2]
    
    round3 = doubleHash(serialNumber)

    for i in range(10):
        for j in range(10):
            if (round3[i] == strs1[j]):
                round3[i] = strs2[(strAsInt + j) % 0x1e]

    return asString(round3)
