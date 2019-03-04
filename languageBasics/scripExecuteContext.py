import sys
import os
from io import StringIO
from subprocess import Popen, PIPE

#cwd and search path
def printCwdAndSearchPath():
    print('cwd: {}'.format(os.getcwd()))
    print('search path: {}'.format(sys.path))
    print('\n')



if __name__ == '__main__':
    #script args
    for i in range(len(sys.argv)):
        print('{} : {}'.format(i, sys.argv[i]))
    print('\n')
   
    #cwd and search path
    oldDir = os.getcwd()
    printCwdAndSearchPath()

    os.chdir('..')
    printCwdAndSearchPath()

    os.chdir(oldDir)
    print('cwd: ' + os.getcwd())
    print('\n')
    
    # input output redirection
    # reassign sys.stdin/stdout/stderr to file like object
    buffer = StringIO()
    oldbuffer = sys.stdout
    sys.stdout = buffer
    print("this msg will not output to teminal")
    print('hello world')
    buffer.write('3.14\n')
    sys.stdout = oldbuffer
    print(buffer.getvalue())
    print('\n')
    
    # print function
    print('this msg will output to stderr stream.', file=sys.stderr)
    print('\n')

    # os.popen function(internal use subprocess Popen)
    pipe = os.popen('python37 helloWorld.py')
    print(type(pipe))
    print(pipe.read())
    pipe.close()
    print('\n')

    os.system('type writer.py')
    print('\n')
    os.system('type reader.py')
    print('\n')
    
    pipW = Popen('python37 writer.py', stdout=PIPE)
    pipR = Popen('python37 reader.py', stdin=pipW.stdout, stdout=PIPE)
    reslut = pipR.communicate()[0]
    print(reslut)

    
    
    #shell environment variable
    # envVarMap = dict(os.environ)
    # print('env variables: ')
    # for pair in envVarMap.items():
    #     print('{} : {}'.format(pair[0], pair[1]), end = '\n')
    



    



