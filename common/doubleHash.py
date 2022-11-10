from common.utils import *
from common.config import *

def doubleHash(input, size=8) -> bytearray:
    md5String = hashFunc(asAscii(input)).digest()

    round1 = bytearray(64)

    for i in range(0, 0x10):
        hexStringOfMd5Byte = bytearray(2)
        md5Entry = asAscii(format(md5String[i], "x"))
        hexStringOfMd5Byte[0:len(md5Entry)] = md5Entry

        if (len(md5Entry) == 1):
            hexStringOfMd5Byte[1] = hexStringOfMd5Byte[0]
        if (i < 1):
            round1[0:2] = hexStringOfMd5Byte
        else:
            concat = (asString(round1) + asString(hexStringOfMd5Byte))
            round1[0:len(concat)] = asAscii(concat)

    dprint("round1: {}".format(asString(round1)))

    md5String = hashFunc(asAscii(asString(round1))).digest()
    round2 = bytearray(64)

    for i in range(0, 0x10):
        hexStringOfMd5Byte = bytearray(2)
        md5Entry = asAscii(format(md5String[i], "x"))
        hexStringOfMd5Byte[0:len(md5Entry)] = md5Entry

        if (len(md5Entry) == 1):
            hexStringOfMd5Byte[1] = hexStringOfMd5Byte[0]
        if (i < 1):
            round2[0:2] = hexStringOfMd5Byte
        else:
            concat = asString(round2) + asString(hexStringOfMd5Byte)
            round2[0:len(concat)] = asAscii(concat)
    
    dprint("round2: {}".format(asString(round2)))

    round3 = bytearray(64)

    for i in range(0, size):
        round3[i] = round2[i * 3]
    
    dprint("round3: {}".format(asString(round3)))

    return round3
