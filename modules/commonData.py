#Common Data
'''
variables
functions
templates
libraires

shared across all modules
can compartamentalize latter

file util,
processor,
library groupings for modules 
---- trust me when you cut down on libs, you save some space.
excessive they may say, but neat, beautiful, clean and readable.
'''
import os,sys,json, shutil
from pathlib import Path
import random as rand


root = Path(os.path.dirname( __file__ ))
savePath = root/"saves"

progDirs = [
    root,
    savePath
]

saveObj = {
"number": 0,
"#steps": 0,
"list": []
}

graphObj = {
    "steps": saveObj["#steps"],
    "name": saveObj["number"],
    "results": saveObj["list"]
}
def cleanPath(location=savePath):
    os.removedirs(location)

def checkProgDirs():
    for d in progDirs:
        if os.path.exists(d):
            pass
        else:
            os.mkdir(d)

'''
gets the current directory disk usage
'''
def getTUF():
    total, used, free = shutil.disk_usage(root)



    print(root)
    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))