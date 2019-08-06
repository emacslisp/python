import sys
import os
import os.path

def main():
    devArray = sys.argv

    if len(devArray) != 2:
        print('pywhere <file>')
        return
    commandName = devArray[1]
    path = os.environ['PATH']
    pathSpliter = "/"
    spliter = ":"
    if os.name == 'nt':
        spliter = ";"
        pathSpliter = "\\"
    paths = path.split(spliter)

    pathDict = {}
    for p in paths:
        targetFilePath = p + pathSpliter + commandName
        if targetFilePath in pathDict:
            continue
        pathDict[targetFilePath] = 1
        if os.path.isfile(targetFilePath):
            print(targetFilePath)

main()