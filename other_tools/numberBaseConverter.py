"""
convert 10-base number to 2-base or 16-base number
"""

import sys
import os

def decToBin(decArr):
    binArr = []
    for num in decArr:
        binArr.append(bin(num))
    return binArr


def binToDec(binArr):
    decArr = []
    for num in binArr:
        decArr.append(int(num, 2))


def decToHex(decArr):
    hexArr = []
    for num in decArr:
        hexArr.append(hex(num))     
    return hexArr


def hexTodec(hexArr):
    decArr = []
    for num in hexArr:
        decArr.append(int(num, 16))
    return decArr


if __name__ == "__main__":
    interactiveMod = True
    if len(sys.argv) > 1:
        interactiveMod = False
    
    decArr = []
    if interactiveMod:
        userinput = input('please input a 10-base integer array, for example 1 2 3:\n')
        temArr = userinput.split()
        try:
            for numStr in temArr:
                decArr.append(int(numStr))
        except Exception as e:
            print('invalid input, exit.')
            os._exit(1)
    else:
        inputfile = sys.argv[1]
        fileinput = open(inputfile, 'r')
        temArr = fileinput.readlines()
        try:
            for line in temArr:
               for numStr in line.split():
                   decArr.append(int(numStr))
        except Exception as e:
            print('invalid input, exit.')
            os._exit(1)
    
    
    print('source input integers: ', decArr)
    userinput = input('please input the number-base to convert to (2 for bin, 16 for hex):\n')
    base = int(userinput)
    tarArr = []
    
    if base == 2:
        tarArr = decToBin(decArr)
    elif base == 16:
        tarArr = decToHex(decArr)
    else:
        print('invalide number base, exit.')
        exit()

    print('target output integers: ', tarArr)

        
