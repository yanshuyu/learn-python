import os
import glob

def osListDir(path, option=''):
    cmds = {'nt':'dir', 'posix':'ls'}
    if not os.name in cmds:
        return []
    return [f for f in os.popen('{} {} {}'.format(cmds[os.name] , path, option))]


def patternListDir(pattern):
    return glob.glob(pattern)


def pyListDir(path):
    return os.listdir(path)


def dirWalk(path, func):
    for (dir, subdirs, files) in os.walk(path):
            func(files)


if __name__ == '__main__':
    # list dir with os specify shell command
    print('os cmd list {}:'.format(os.getcwd()))
    for line in osListDir(os.curdir, '*.py'):
        print(' ',line)

    
    # list dir with glob module
    print('pattern matching list {}:'.format(os.getcwd()))
    for line in patternListDir(os.getcwd()+'/*.py'):
        pathPrefix, fname = os.path.split(line)
        print('\t', line, '\t', fname)
    
    oldCwd = os.getcwd()
    os.chdir(os.pardir)
    print('parttern matching list {}:'.format(os.getcwd()))
    for line in patternListDir('*.txt'):
        print('\t', line)
    os.chdir(oldCwd)

    # list dir with os.listdir
    print('python routine list {}:'.format(os.getcwd()))
    for line in pyListDir(os.getcwd()):
        fullpath = os.path.join(os.getcwd(), line)
        print('\t', line, '\t', fullpath)

 
    alljpgs = []
    def selectJpg(files):
        for file in files:
            if file.endswith('.jpg'):
                alljpgs.append(file)

    dirWalk(r'E:\y1\client\trunk\develop\res\common', selectJpg)
    print('all jpg fils:', alljpgs)