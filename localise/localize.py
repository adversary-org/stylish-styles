#! /usr/bin/env python

# CSS Localiser (CSS Localizer)
# Version 1.0
#
# Copyright (C) Ben McGinnes, 2014
# Email:  ben@adversary.org
# GPG Key:  0x321E4E2373590E5D
# License:  GPLv3 or any later version
# Website:  https://github.com/adversary-org/stylish-styles
# Bitcoin:  17VvZDeLjhiH1ccU6rZWLZc41UiZd8eh6F
#
# Takes a file, downloads all the GIFs, JPGs and PNGs, then copies or
# moves them to a custom directory (here specific to the Stylish
# extension) and rewrites the file with the images local URLs called.
# Intended for use with CSS files and specifically for Stylish themes,
# but will run on any file it can open (though it includes the CSS
# data tags, so it might not help with other file types really).
#
# Since it's basically the same as localise.py except without the
# base64 encoding, the very slight name change seemed appropriate.
#
# Written and tested with Python 2.7, probably works with some earlier
# versions and will almost certainly require some degree of
# modification to work with Python 3.  There are a ridiculous number
# of references to The Chronicles of Amber by Roger Zelazny too, do
# yourself a favour and go read that instead of this code.
#
# Usage: ./localize.py your_theme.css
#
# Output will be: new_your_theme.css and the image files downloaded to
# the specified directory (a hidden folder on Linux and OS X).
#
#
# CSS Localizer: downloads, coverts and embeds images as base64 data.
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

import os
import os.path
import re
import requests
import sys

sa = sys.argv[1]

home = os.path.expanduser("~")
windir = "\\Stylish\\"
nixdir = "/.stylish/"
curdir = os.path.abspath(".")
infile = os.path.abspath(sa)
outfile = os.path.abspath(curdir + "/new_" + sa)

if sys.platform is "linux" or "linux2" or "darwin":
    styledir = home + nixdir
    themedir = styledir + sa.replace(".", "-") + "/"
elif sys.platform is "win32":
    styledir = home + windir
    themedir = styledir + sa.replace(".", "-") + "\\"
else:
    styledir = home + nixdir
    themedir = styledir + sa.replace(".", "-") + "/"

if os.path.exists(styledir) is not True:
    os.mkdir(styledir)
else:
    pass

if os.path.exists(themedir) is not True:
    os.mkdir(themedir)
else:
    pass

f = open(infile, "r")
lines = f.readlines()
f.close()

unicorn = []

for line in lines:
    pattern = re.findall(r"(https?://[^\s]+)", line)
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
            rhead = "file:///"
            pit = themedir + tail
            chaos = rhead + pit
            trump = open(pit, "wb")
            trump.write(rorder.content)
            trump.close()
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
