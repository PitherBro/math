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
    saveFile = open(savePath/f'val-{initNum}.json','w')
    print(json.dumps(output,indent=2), file=saveFile)
    saveFile.close()
def genNumber(minMax = (2,100)):
    
    initNum = rand.randint(minMax[0],minMax[1])# int(input("Enter a number greater than 2: "))
    knowns = []
    while checkPastRuns(initNum):
        initNum = rand.randint(minMax[0],minMax[1])
        print(f"run{initNum}")
    return initNum
def genMenuSelection():
    options = [

    ]
    optDisplay = ""
    for i in options:
        pass






if __name__ == "__main__":
    checkProgDirs()
    ask = int(input("how big of a number?\nMust be greater than 2."))
    for x in range(ask):
        num = genNumber()
        runMathFunc(num)
    #print(__name__)
    #print(sys.argv)    
    #print(sys.path)
    #pass
    
    

    #print(json.loads(json.dumps(output)))

    

#save results on threads -> cores -> chunked json files with time stamp folders w interval and batchSize
#hook up a stat output
#node web express coupled with suppa backend?
#display multiple graphs for comparisons, import curve funcs for randomness vals
#run bursts till overall goal is complete, set size=intervalXbatch, 
