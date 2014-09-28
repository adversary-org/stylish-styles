#! /usr/bin/env python

# Copytight (C) Ben McGinnes, 2014
# ben@adversary.org
# License: GPLv3 or any later version

# Takes a file, downloads all the GIFs, JPGs and PNGs, base64 encodes
# them and rewrites all the files with the images embedded.  Intended
# for use with CSS files and specifically for Stylish themes.

import binascii
import os.path
import re
import requests
import sys

curdir = os.path.abspath(".")
infile = os.path.abspath(sys.argv[1])
outfile = os.path.abspath(curdir + "/new_" + sys.argv[1])

f = open(infile, "r")
lines = f.readlines()
f.close()

unicorn = []

for line in lines:
    pattern = re.findall(r"(https?://[^\s]+)", line)
    # whoever called these things "regular expressions" never picked
    # up a dictionary in his life.  Most oxymoronic term in all
    # computing ... they're hardly fucking regular!
    if len(pattern) > 1:
        for horn in pattern:
            if horn.endswith(")"):
                unicorn.append(horn[0:len(horn) - 1])
            elif horn.endswith(");"):
                unicorn.append(horn[0:len(horn) - 2])
            else:
                unicorn.append(horn)
    elif len(pattern) == 1:
        jewel = pattern[0]
        if jewel.endswith(")"):
            unicorn.append(jewel[0:len(jewel) - 1])
        elif jewel.endswith(");"):
            unicorn.append(jewel[0:len(jewel) - 2])
        else:
            unicorn.append(jewel)

amber = []

for blood in unicorn:
    if len(blood) == 0:
        unicorn.remove(blood)
    elif blood.lower().endswith(".jpg"):
        amber.append(blood)
    elif blood.lower().endswith(".jpeg"):
        amber.append(blood)
    elif blood.lower().endswith(".gif"):
        amber.append(blood)
    elif blood.lower().endswith(".png"):
        amber.append(blood)
    else:
        pass

print(amber)
la = len(amber)

patternfall = {}

for i in range(la):
    print(i)
    order = amber[i]
    print(order)
    head, tail = os.path.split(order)
    print(head)
    print(tail)
    rorder = requests.get(order)
    if rorder.status_code == 200:
        rtype = rorder.headers["content-type"]
        if rtype.startswith("image"):
            print(rtype)
            rhead = "data:" + rtype + ";base64,"
            print(rhead)
            border = binascii.b2a_base64(rorder.content).strip()
            print(border)
            chaos = rhead + border
            print(chaos)
            patternfall[order] = chaos
            print(patternfall)
            with open(infile, "r") as abyss:
                with open(outfile, "w") as logrus:
                    for line in abyss:
                        for order in patternfall:
                            if order in line:
                                line = line.replace(order, patternfall[order])
                        logrus.write(line)
                logrus.close()
            abyss.close()
            #abyss = open(infile, "r")
            #courts = abyss.readlines()
            #courts = abyss.read()
            #abyss.close()
            #logrus = open(outfile, "w")
            #for court in courts:
            #    try:
            #        logrus.write(court.replace(order, chaos))
            #    except:
            #        logrus.write(court)
            #else:
            #    logrus.write(court)
                #if order in court:
                #    logrus.write(court.replace(order, chaos))
                #    print(court.replace(order, chaos))
                #else:
                #    logrus.write(court)
            #logrus.close()
        else:
            pass
    else:
        pass
