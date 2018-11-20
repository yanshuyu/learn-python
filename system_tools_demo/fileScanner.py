import os
import sys
import pprint

def fileScanner(dir, ext, trace=0):
    """
        scan file by extension at root dir recursively.
        trace (0-off 1-trace dir, >2-trace dir and files)
    """
    dir = os.path.normpath(dir)
    dir = os.path.normcase(dir)
    visited = set()
    allFiles = []
    for (rootdir, subdirs, files) in os.walk(dir):
        if rootdir in visited:
            if trace > 0:
                print('skip dir "' + rootdir + '" ...')
            continue
        else:
            if trace > 0:
                print('scanning dir "' + rootdir +'" ...')
            visited.add(rootdir)
            for fname in files:
                if fname.endswith(ext):
                    fullname = os.path.join(rootdir, fname)
                    if trace > 1:
                        print('checking file "' + fullname + '" ...')
                    size = os.path.getsize(fullname)
                    line = 0
                    for _ in open(fullname, 'rb'):
                        line += 1
                    allFiles.append((fullname, size, line))
              

    return allFiles



if __name__ == '__main__':
    dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    ext = sys.argv[2] if len(sys.argv) > 2 else '.py'
    trace = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    allFiles = fileScanner(dir, ext, trace)

    allFiles.sort(key = lambda item : item[1])
    print('sorted by size: ')
    pprint.pprint(allFiles[:3])
    pprint.pprint(allFiles[-3:])

    allFiles.sort(key = lambda item : item[2])
    print('sorted by lines: ')
    pprint.pprint(allFiles[:3])
    pprint.pprint(allFiles[-3:])