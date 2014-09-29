#! /usr/bin/env python

# CSS Localiser
# Version 1.0
#
# Copyright (C) Ben McGinnes, 2014
# Email:  ben@adversary.org
# GPG Key:  0x321E4E2373590E5D
# License:  GPLv3 or any later version
# Website:  https://github.com/adversary-org/stylish-styles
#
# Takes a file, downloads all the GIFs, JPGs and PNGs, base64 encodes
# them and rewrites the file with the images embedded.  Intended for
# use with CSS files and specifically for Stylish themes, but will run
# on any file it can open (though it includes the CSS data tags, so it
# might not help with other file types really).
#
# Written and tested with Python 2.7, probably works with some earlier
# versions and will almost certainly require some degree of
# modification to work with Python 3.  There are a ridiculous number
# of references to The Chronicles of Amber by Roger Zelazny too, do
# yourself a favour and go read that instead of this code.
#
# Usage: ./localiser.py your_theme.css
#
# Output will be: new_your_theme.css
#
#
# CSS Localiser: downloads, coverts and embeds images as base64 data.
# Copyright (C) 2014  Ben McGinnes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# The license is available in the GitHub repository along with the
# rest of my CSS theme work:
#
# https://github.com/adversary-org/stylish-styles/blob/master/LICENSE.txt
##

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

la = len(amber)

patternfall = {}

for i in range(la):
    order = amber[i]
    head, tail = os.path.split(order)
    rorder = requests.get(order)
    if rorder.status_code == 200:
        rtype = rorder.headers["content-type"]
        if rtype.startswith("image"):
            rhead = "data:" + rtype + ";base64,"
            border = binascii.b2a_base64(rorder.content).strip()
            chaos = rhead + border
            patternfall[order] = chaos
            with open(infile, "r") as abyss:
                with open(outfile, "w") as logrus:
                    for serpent in abyss:
                        for order in patternfall:
                            if order in serpent:
                                serpent = re.sub(order, patternfall[order], serpent)
                        logrus.write(serpent)
                logrus.close()
            abyss.close()
        else:
            pass
    else:
        pass
