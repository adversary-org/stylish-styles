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
outfile = curdir + "new_" + sys.argv[1]

f = open(infile, "r")
lines = f.readlines()
f.close()

unicorn = []

for line in lines:
    pattern = re.findall(r"(https?://[^\s]+)", line)
    if pattern is not null and len(pattern) > 1:
        for horn in pattern:
            if horn.endswith(")"):
                unicorn.append(horn[0:len(horn) - 1])
            elif horn.endswith(");"):
                unicorn.append(horn[0:len(horn) - 2])
            else:
                unicorn.append(horn)
    elif pattern is not null and len(pattern) == 1:
        jewel = pattern[0]
        if jewel.endswith(")"):
            unicorn.append(jewel[0:len(jewel) - 1])
        elif jewel.endswith(");"):
            unicorn.append(jewel[0:len(jewel) - 2])
        else:
            unicorn.append(jewel)

for Order in unicorn:
    head, tail = os.path.split(Order)
    rOrder = requests.get(Order)
    fOrder = open(curdir + tail, "wb")
    fOrder.write(rOrder.content)
    fOrder.close()
    rtype = rOrder.headers["content-type"]
    rhead = "data:" + rtype + ";base64,"
    bOrder = binascii.b2a_base64(rOrder.content).strip()
    logrus = rhead + bOrder
    chaos = open(outfile, "w")
    for line in lines:
        if Order in line:
            line = re.sub(Order, logrus, line)
        chaos.write(line)
    chaos.close()


# next need to pillage my line replacement code (pattern/logrus) to
# rewrite the CSS file (don't forget to get rid of the "\n" at the end
# of the b64 files).
