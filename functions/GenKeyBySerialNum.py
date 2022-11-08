from doubleHash import *
from config import *
from binUtils import *

strs1 = asAscii("125690IOSZ")
strs2 = asAscii("3478ABCDEFGHJKLMNPQRTUVWXY")

def zcfgBeCommonGenKeyBySerialNum(inputKey: str, serialNumber: str) -> str:
    md5Result = hashFunc(asAscii(serialNumber)).digest()
    md5Result = hashFunc(asAscii("{}PSK_ra0{}".format(inputKey, md5Result))).digest()

    #strAsInt = (asInt(md5Result) >> 0x18) * 0x100 + (asInt(md5Result) >> 0x10 & 0xff)
    strAsInt = (md5Result[1] << 8) + md5Result[2]
    round1 = bytearray(40)
    local_b8 = 1

    for i in range(10):
        assignInt(round1, i * 4,  (strAsInt % (local_b8 << 1)) // local_b8)
        local_b8 = local_b8 << 1
    
    offset = 0
    round2 = bytearray(11)

    for i in range(10):
        char: str
        if (asInt(round1, i * 4) == 1):
            char = format(md5Result[i] % 0x1a + 0x41, "c") 
        else:
            md5Byte = md5Result[i]
            char = format((md5Byte - ((md5Byte // 10) * 2 + ((md5Byte * 0xcccccccd >> 0x20) & 0xfffffff8)) & 0xff) + 0x30, "c")
        
        round2[offset:offset + len(char)] = asAscii(char)
        offset = offset + len(char)

        for j in range(10):
            if (round2[i] == strs1[j]):
                round2[i] = strs2[j]
                break
    
    output = bytearray(64)

    assignInt(output, 0, asInt(round2))
    assignInt(output, 4, asInt(round2, 4))

    output[8] = round2[8]
    output[9] = round2[9]

    return asString(output)