#!/usr/bin/python3

from os import listdir, path
import sys

from functions.GenKeyBySerialNum import *
from functions.GenKeyBySerialNum_CBT import *
from functions.GenKeyBySerialNumConfigLength import *
from functions.GenKeyBySerialNumConfigLengthOld import *
from functions.GenKeyBySerialNumMethod2 import *
from functions.GenKeyBySerialNumMethod3 import *
from functions.IsApplyRandomAdminPasswordNewAlgorithm import *

currentDir = path.dirname(path.realpath(__file__))
testDir = path.join(currentDir, "tests")

anyFailed = False

for testFile in listdir(testDir):
    serialNumber = testFile[0:-4]
    testFile = path.join(testDir, testFile)
    contents = open(testFile, "r").read()

    print(serialNumber)
    for line in contents.split("\n"):
        if (len(line) == 0): continue

        expectedSeperator = line.index(": ")

        params = "\"" + serialNumber + "\""
        extraParams = ""
        function = ""
        if (not "(" in line[:expectedSeperator]):
            function = line[:expectedSeperator]
        else:
            paramsStart = line.index("(") + 1
            paramsEnd = line.index(")")
            function = line[:paramsStart - 1]
            extraParams = line[paramsStart: paramsEnd]
            params = params + ", " + extraParams
        
        expected = line[expectedSeperator + 2:]

        trimmedFunctionName = function[12:]

        try:
            result = eval(function + "(" + params + ")")
            lastParam = extraParams[-1] if len(extraParams) > 0 else ""
            testName = trimmedFunctionName + "(" + lastParam + ")"
            if (expected != result):
                print("    \033[91mFail\033[0m: {:36}: expected \033[96m{:>8}\033[0m but got \033[96m{:>8}\033[0m".format(testName, expected, result))
                anyFailed = True
            else:
                print("    \033[92mPass\033[0m: {}".format(testName))
        except NameError:
            continue

if (anyFailed):
    exitCode = 1
else:
    exitCode = 0

sys.exit(exitCode)
