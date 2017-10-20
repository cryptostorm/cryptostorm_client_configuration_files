#!/usr/bin/python

import subprocess
from os import listdir
from os.path import isfile, join
import re
import os
import sys
import time

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--extraparams', metavar='N', type=str, nargs='+',
                            help='any params to be passed to openvpn')
parser.add_argument('--killswitch', action="store_true", default=False)
parser.add_argument('--disable_killswitch', action="store_true", default=False)

args = parser.parse_args()

print args

dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path

if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

## disable kill switch
if args.disable_killswitch:
    subprocess.check_call(dir_path + "/kill_switch.sh", shell=True)
    sys.exit(0)

p = re.compile('(cstorm_linux-|\.ovpn)') 

def extract(f):
    return p.sub('', f)

configs = [f for f in listdir(dir_path) if (isfile(join(dir_path, f)) and ".ovpn" in f)]
configs.sort()

maxIndex = 0
for f in configs:
    print maxIndex, extract(f)
    maxIndex += 1

user_selection = 0
user_input = ""
while user_input == "":
    print "Connect to [0]:",
    user_input = raw_input()
    try:
        conv = int(user_input)
        if conv >= 0 and conv < maxIndex:
            user_selection = conv
            break
    except ValueError:
        pass
    user_input = ""

cstorm_config = configs[user_selection]
print "user chose", extract(cstorm_config)

auth_file = dir_path + "/" + "auth.conf"

cmd = "openvpn --config " + dir_path + "/" + cstorm_config

if isfile(auth_file):
    cmd += " --auth-user-pass " + auth_file

if args.extraparams is not None:
    for p in args.extraparams:
        cmd += " " + p

print "starting openvpn with", cmd
openvpn = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print "connecting"

time.sleep(5)

## now that we're connected enable kill switch
if args.killswitch:
    subprocess.check_call(dir_path + "/kill_switch.sh ENABLE", shell=True)

print "connected"
print "press any key to terminate",
raw_input()
print "terminating"

openvpn.terminate()

def get_openvpn_procs():
    try:
        procs = subprocess.check_output("ps aux | grep '.*openvpn.*" + cstorm_config + ".*' | grep -v grep", shell=True)
        return procs
    except subprocess.CalledProcessError:
        return ""

def terminate_all_openvpn():
    procs = get_openvpn_procs()
    if procs == "":
        return
    sleep_count = 0
    while procs != "":
        procs_split = procs.split("\n")
        #print procs_split
        for p in procs_split:
            stuff = p.split()
            if not stuff:
                continue
            #print stuff[1]
            kill = "kill "
            if sleep_count == 6:
                kill = "kill -9 "
            subprocess.call(kill + stuff[1], shell=True)
        
        time.sleep(5)
        sleep_count += 1
        procs = get_openvpn_procs()

terminate_all_openvpn()
print "terminated"
subprocess.check_call(dir_path + "/kill_switch.sh", shell=True)
