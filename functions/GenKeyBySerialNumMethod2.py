from common.utils import asString
from common.doubleHash import *

def zcfgBeCommonGenKeyBySerialNumMethod2(serialNumber):
    round3 = doubleHash(serialNumber)
    
    return asString(round3)
