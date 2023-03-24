#!/bin/python3
args = sys.argv

from modules.commonData import *

def setPaths():
    for p in progDirs:
        sys.path.append(p)

setPaths()

import progLoop as pl

pl.cleanPath()