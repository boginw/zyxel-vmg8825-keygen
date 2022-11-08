from binUtils import asString
from doubleHash import *

def zcfgBeCommonGenKeyBySerialNumMethod2(serialNumber):
    round3 = doubleHash(serialNumber)
    
    return asString(round3)
