import struct
from common.config import *
import inspect

ended = True

def asInt(bytes: bytes, start: int = 0) -> int:
    global endian
    if (endian == "big"):
        return struct.unpack_from(">I", bytes, start)[0]
    else:
        return struct.unpack_from("<I", bytes, start)[0]

def assignInt(var: bytearray, start: int, val: int):
    global endian
    if (endian == "big"):
        struct.pack_into(">I", var, start, val)
    else:
        struct.pack_into("<I", var, start, val)

def uppercaseBytearray(byteArray: bytearray):
    uppercase = asAscii(asString(byteArray).upper())
    byteArray = bytearray(64)
    byteArray[0:len(uppercase)] = uppercase
    return byteArray

def asAscii(string: str) -> bytes:
    return string.encode("ascii")

def asString(bytes: bytes) -> str:
    return bytes.decode("ascii").rstrip("\x00")

def asChar(string: str) -> int:
    return asAscii(string)[0]

def char(bytes: bytes, start: int = 0):
    global endian
    if (endian == "big"):
        return int.from_bytes(struct.unpack_from(">c", bytes, start)[0], "big")
    else:
        return int.from_bytes(struct.unpack_from("<c", bytes, start)[0], "little")

def dprint(
    *values: object,
    sep: str = None,
    end: str = None,
    flush: bool = False,
) -> None:
    global debug, ended
    if (debug):
        if (ended and len(values) > 0):
            print("\033[94m", end="")
            print(inspect.stack()[1][0].f_code.co_name[-32:], end=": ")
            print("\033[0m", end="")
        
        ended = end == None or "\n" in end
        print(*values, sep = sep, end = end, flush = flush)
