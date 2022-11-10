#!/usr/bin/python3

import argparse
import sys
import common.config

parser = argparse.ArgumentParser()
parser.add_argument("serial", help="Serial number of the router")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-f", "--function", help="function to run")
args = parser.parse_args()

if (args.verbose):
    common.config.debug = True

from functions.GenKeyBySerialNum import *
from functions.GenKeyBySerialNum_CBT import *
from functions.GenKeyBySerialNumMethod2 import *
from functions.GenKeyBySerialNumMethod3 import *
from functions.GenKeyBySerialNumConfigLength import *
from functions.GenKeyBySerialNumConfigLengthOld import *

functionFound = False

def run(key: str, f):
    global args, functionFound
    if (args.function == None or args.function == key):
        print("{:48}: {}".format(key, f()))
        functionFound = True

key = common.config.defaultInputKey
serial = args.serial

run("zcfgBeCommonGenKeyBySerialNum", lambda: zcfgBeCommonGenKeyBySerialNum(serial, key))
run("zcfgBeCommonGenKeyBySerialNum_CBT", lambda: zcfgBeCommonGenKeyBySerialNum_CBT(serial))
run("zcfgBeCommonGenKeyBySerialNumMethod2", lambda: zcfgBeCommonGenKeyBySerialNumMethod2(serial))
run("zcfgBeCommonGenKeyBySerialNumMethod3", lambda: zcfgBeCommonGenKeyBySerialNumMethod3(serial))
run("zcfgBeCommonGenKeyBySerialNumConfigLength(1)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLength(serial, key, 8, 1))
run("zcfgBeCommonGenKeyBySerialNumConfigLength(2)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLength(serial, key, 8, 2))
run("zcfgBeCommonGenKeyBySerialNumConfigLength(3)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLength(serial, key, 8, 3))
run("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(1)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serial, key, 8, 1))
run("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(2)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serial, key, 8, 2))
run("zcfgBeCommonGenKeyBySerialNumConfigLengthOld(3)", lambda: zcfgBeCommonGenKeyBySerialNumConfigLengthOld(serial, key, 8, 3))

if (not functionFound):
    print("Could not find function: " + args.function)
    parser.print_usage()
    sys.exit()
