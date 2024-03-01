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
-----
trust me when you cut down on libs, you save some space.
excessive it may be, but neat, beautiful, clean and readable = good code.
'''
import os,sys,json, shutil
from pathlib import Path
import random as rand

#gets the root directory of app.
root = Path(os.path.dirname( __file__ )).parent
savePath = root/"sampleRuns"
sp3xPlusOne = savePath/'3x+1'
progInitPath = root/'progInit.py'


#
progDirs = [
    root,
    savePath,
    sp3xPlusOne,
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
def cleanPath(location=sp3xPlusOne):
    #print(location)
    for f in os.listdir(location):
        if Path.is_file(f):
            print(f)
        # os.removedirs(location)

#check if each program directory requiered to oppereate exists.
def checkProgDirs():
    '''
    Runs through the list of required program directires\n
    Creates the directory if missing, does nothing if it exists.
    '''
    for d in progDirs:
        if os.path.exists(d):
            pass
        else:
            os.mkdir(d)

def getTUF():
    '''
Gets the current directory disk usage in Gigabits
T: total
U: unused
F: Free
'''
    total, used, free = shutil.disk_usage(root)



    print(root)
    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))