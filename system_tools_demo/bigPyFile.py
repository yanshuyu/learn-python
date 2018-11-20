import sys
import os
import glob
import pprint


def searchBigPy(dir, rec=False):
    """
        Search biggest and smallest .py file in a dir
    """
    allPy = []
    searchPattern = os.path.join(dir, '**','*.py') if rec else os.path.join(dir,'*.py') 
    for pyFile in glob.glob(searchPattern,recursive=rec):
        allPy.append((pyFile, os.path.getsize(pyFile)))
    if len(allPy) > 0:
        allPy.sort(key = lambda item : item[1])
    return allPy

if __name__ == "__main__":
    #searchDir = sys.exec_prefix if len(sys.argv) == 1 else sys.argv[1]
    searchDir = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]
    print('search path: ',searchDir)
    allPyFiles = searchBigPy(searchDir, True)
    print('two biggest result: ')
    pprint.pprint(allPyFiles[-2:])
    print('two smallest result: ')
    pprint.pprint(allPyFiles[:2])