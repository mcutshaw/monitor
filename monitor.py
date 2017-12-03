#!/usr/bin/python3
import sys
import subprocess

max_fails = 20

if(len(sys.argv)) < 2:
    print("Usage: "+str(sys.argv[0])+" \"COMMAND\"")
    exit()
args = str(sys.argv[1])
while(1):
    try:
        proc = subprocess.Popen(args,shell=True)
        proc.wait()
        max_fails-=1
        if(max_fails == 0):
            print("Max Failures exceeded, exiting")
            exit()
    except Exception as ex:
        print("Exeception: "+str(ex))
