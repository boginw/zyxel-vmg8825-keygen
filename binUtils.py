import struct
from config import *

def asInt(bytes: bytearray | bytes, start: int = 0) -> int:
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

def char(bytes: bytearray | bytes, start: int = 0):
    global endian
    if (endian == "big"):
        return int.from_bytes(struct.unpack_from(">c", bytes, start)[0], "big")
    else:
        return int.from_bytes(struct.unpack_from("<c", bytes, start)[0], "little")
