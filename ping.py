import os
import platform
import json

SUCCESS="SUCCESS"
FAILED="FAILED"
output_dict=dict()

def add(key,value):
    output_dict[key]=value

def checkHost(HOST):
    if platform.system() == "Windows":
        response = os.system("ping "+HOST+" -n 1")
    else:
        response = os.system("ping -c 1 " +HOST)

    if response == 0:
        add(HOST, SUCCESS)
    else:
        add(HOST, FAILED)

def host():
    checkHost("216.58.197.46")
    checkHost("172.217.163.164")
    checkHost("www.google.co")
    checkHost("www.google.c")


def run():
    host()
    with open("output.json", "w") as outfile:
        json.dump(output_dict, outfile)
run()