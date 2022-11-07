#!/usr/bin/python3

import sys
from GenKeyBySerialNum import *
from GenKeyBySerialNum_CBT import *
from GenKeyBySerialNumMethod2 import *
from GenKeyBySerialNumMethod3 import *
from GenKeyBySerialNumConfigLength import *
from GenKeyBySerialNumConfigLengthOld import *

serialNumber = sys.argv[1]

res1 = zcfgBeCommonGenKeyBySerialNum("inputKey", serialNumber)
res2 = zcfgBeCommonGenKeyBySerialNum_CBT(serialNumber)
res3 = zcfgBeCommonGenKeyBySerialNumMethod2(serialNumber)
res4 = zcfgBeCommonGenKeyBySerialNumMethod3(serialNumber)
res5 = zcfgBeCommonGenKeyBySerialNumConfigLength(serialNumber, 8, 1)
res6 = zcfgBeCommonGenKeyBySerialNumConfigLength(serialNumber, 8, 2)
res7 = zcfgBeCommonGenKeyBySerialNumConfigLength(serialNumber, 8, 3)
res8 = zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serialNumber, "inputKey", 8, 1)
res9 = zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serialNumber, "inputKey", 8, 2)
resA = zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serialNumber, "inputKey", 8, 3)

print("zcfgBeCommonGenKeyBySerialNum:                   {}".format(res1))
print("zcfgBeCommonGenKeyBySerialNum_CBT:               {}".format(res2))
print("zcfgBeCommonGenKeyBySerialNumMethod2:            {}".format(res3))
print("zcfgBeCommonGenKeyBySerialNumMethod3:            {}".format(res4))
print("zcfgBeCommonGenKeyBySerialNumConfigLength(1):    {}".format(res5))
print("zcfgBeCommonGenKeyBySerialNumConfigLength(2):    {}".format(res6))
print("zcfgBeCommonGenKeyBySerialNumConfigLength(3):    {}".format(res7))
print("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(1): {}".format(res8))
print("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(2): {}".format(res9))
print("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(3): {}".format(resA))
