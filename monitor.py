#!/usr/bin/python3
import sys
import subprocess

max_fails = 20

if(len(sys.argv)) < 2:
    print("Usage: "+str(sys.argv[0])+" \"COMMAND\" LOGFILE")
    exit()
args = str(sys.argv[1])
while(1):
    try:
        subprocess.call(args,shell=True)
        max_fails-=1
        if(max_fails == 0):
            print("Max Failures exceeded, exiting")
            exit()
    except Exception as ex:
        print("Exeception: "+str(ex))
