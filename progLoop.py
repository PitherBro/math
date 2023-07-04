#!/bin/python3
#Program Loop
"""
This function runs the 3x+1 algorithm,
it runs on the assumption that if x is even we divide it by 2
if x is odd we multiply by 3 then add 1

this is just a fun math problem which yeilds interesting results the larger your problem.
this algorithm jaggedly jumps then skips to a 4,2,1 loop...which we stop.

each run is randomly generated and saved as a json file.
"""
from modules.commonData import *
import math
from threading import Thread




def func(x=2):
    #lets the function run at the minimum required if it was incorrectly inputed
    #for security we could exit the function at this juncture, or ask again.
    if x < 2:
        x = 2
    #stores each itteration of the program
    results = []
    while x >=4:
        #even
        if x % 2 ==0:
            # x/2
            x = x/2
            
        #odd
        else:
            #x*3 +1
            x =(x *3) +1
            
        results.append(x)
    return results
def checkPastRuns(num, file="val-{num}.json"):
    if not file:
        isFile = os.path.isfile(savePath/f"val-{num}.json")
        if not isFile:
            return False
        
    elif file:
        isFile = os.path.isfile(file)
        return False
def runMathFunc(initNum):
    r = func(initNum)
    #print(r)
    #print(f"initail num: {initNum}\n#divisions:{len(r)}")
    output = {
        "number": initNum,
        "#steps": len(r),
        "list": r
    }
    print(output["number"])
    saveFile = open(sp3xPlusOne/f'val-{initNum}.json','w')
    print(json.dumps(output,indent=2), file=saveFile)
    saveFile.close()
def genRandNumber(minMax = (2,100)):
    '''
    generates a random number between a Tuple passed,\n
    checks against saveFile directory to see if number was made before.
    if it does, it makes a unique one. 
    '''
    initNum = rand.randint(minMax[0],minMax[1])# int(input("Enter a number greater than 2: "))
    knowns = []
    while checkPastRuns(initNum):
        initNum = rand.randint(minMax[0],minMax[1])
        print(f"run{initNum}")
    return initNum

def genMenuSelection():
    \
'''
simple [index]: {choice},selection\n
allows easy feed of information.
'''
    options = [
        "exit",
        "random",
        "your number, punk",
        "see Graph",
        "see Graphs"
    ]
    optDisplay = ""
    for i in range(len(options)):
        #formats as single block,
        #leaves last line clear of new line command
        
        if i == -1+len(options):
            optDisplay += f"{i}: {options[i]}"
        else:
            optDisplay += f"{i}: {options[i]}\n"
    return optDisplay

def selectMenu():
    '''
the call to make a menu call.\n
returns choice as index selection
    '''
    options = genMenuSelection()

    print(genMenuSelection())
    ask = int(input(f"Which opperation we wanting to complete today?[0-{len(options.split())-1}]"))
    return ask

def processMenu(choice=0):
    options = genMenuSelection().split('\n')

    if choice == 0:
        pass
    options[choice]
    pass

def isOpts(selection=0):
    max=len(genMenuSelection())-1
    if selection >= 0 or selection <=max:
        return True
    else:
        False




#should just do some checks
#migrate program to init.
#build logic tree
if __name__ == "__main__":

    #pre loop execution:
    checkProgDirs()
    #print(__name__)
    #print(sys.argv)    
    #print(sys.path)
    #pass
    
    '''
    a bit of insainity to chain commands.
    or handle arguments.
    lets make the program read forward and backward.
    chain commands, call again to execute on explosive demand...recursive.
    
    '''
    ask =0
    opts = []

    while not ask == 0 :
        ask = int(selectMenu())
        if isOpts(ask):
            opts.append(ask)
        
    for x in range(opts):
        num = genRandNumber()
        runMathFunc(num)
    
    
    ask = input("remove calculation data? may require admin prvilage(y/n)") or "n"
    if ask == 'n':
        pass
    if ask == 'y':
        cleanPath()
    

    #print(json.loads(json.dumps(output)))

    

#save results on threads -> cores -> chunked json files with time stamp folders w interval and batchSize
#hook up a stat output
#node web express coupled with suppa backend?
#display multiple graphs for comparisons, import curve funcs for randomness vals
#run bursts till overall goal is complete, set size=intervalXbatch, 
