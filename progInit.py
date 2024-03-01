#!/bin/python3
args = sys.argv

from modules.commonData import *

'''
This file should serve as the main entrance, and selection of tasks to run.
- Generate data for 3x+1
- show graphical data for a run
- try a diffrent sort of function to generate data from


progLoop needs to configured for user input or a list of numbers to run the 3x+1 algorithem
plotGraph, needs an consoles interface to select a graph
    - later can save `.png` of a graph to embed into a webpage
'''

def setPaths():
    for p in progDirs:
        sys.path.append(p)

setPaths()

import progLoop as pl

pl.cleanPath()