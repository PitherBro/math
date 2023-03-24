#!/bin/bash
currentDir=$(pwd)
echo $currentDir
#python3 is native, easy.
#no depenendies to install because all native code, no imported libs.
exec python3 $currentDir/progInit.py