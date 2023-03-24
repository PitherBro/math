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
excessive it may be, but neat, beautiful, clean and readable = good code.
'''
import os,sys,json, shutil
from pathlib import Path
import random as rand


root = Path(os.path.dirname( __file__ )).parent
savePath = root/"saves"
progInitPath = root/'progInit.py'
#
progDirs = [
    root,
    savePath,
    progInitPath
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
#should delete a 
#by default cleans up the save files
def cleanPath(location=savePath):
    #print(location)
    os.removedirs(location)

#check if each program directory requiered to oppereate exists.
def checkProgDirs():

    for d in progDirs:
        if os.path.exists(d):
            pass
        else:
            os.mkdir(d)

def getTUF():
    '''
gets the current directory disk usage
'''
    total, used, free = shutil.disk_usage(root)



    print(root)
    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))