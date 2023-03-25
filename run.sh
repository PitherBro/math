#!/bin/bash
currentDir=$(pwd)
pyLib=$currentDir/langs/python/python.exe

echo "Working From-> $currentDir"
echo "pyLib-> $pyLib"
#python3 is native, easy.
#no depenendies to install because all native code, no imported libs.
#exec python3 $currentDir/progInit.py
$pyLib "$currentDir/progInit.py"

