#! /usr/bin/env python

# Copytight © Ben McGinnes, 2014
# ben@adversary.org
# License: GPLv3 or any later version

# Takes a file, downloads all the GIFs, JPGs and PNGs, base64 encodes
# them and rewrites all the files with the images embedded.  Intended
# for use with CSS files and specifically for Stylish themes.

import base64
import os.path
import re
import requests
import sys

curdir = os.path.abspath(".")
infile = os.path.abspath(sys.argv[1])

f1 = open(infile, "r")
lines = f1.readlines()
f1.close()

url_list = infile + ".tmp1.txt"

f2 = open(url_list, "w")
for line in lines:
    f2.write(re.findall('url\(([^)]+)\)', line))
f2.close()

f3 = open(url_list, "r")
pics = f3.readlines()
f3.close()

for pic in pics:
    rpic = requests.get(pic)
    head, tail = os.path.split(rpic.url)
    fpic = open(curdir + tail, "wb")
    fpic.write(rpic.content)
    fpic.close()
    base64.encode(curdir + tail, curdir + tail + ".base64")

# next need to pillage my line replacement code (pattern/logrus) to
# rewrite the CSS file (don't forget to get rid of the "\n" at the end
# of the b64 files).
