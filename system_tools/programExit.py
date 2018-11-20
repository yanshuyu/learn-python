import sys
import os
import subprocess

if __name__ == '__main__':
    choice = '0'
 
    choice = input('input exit choice: 1 for sys.exit() 2 or os._exit()\n')

    #sys.exit()会抛出异常
    if choice == '1':
        try:
            sys.exit(-10)
        except SystemExit as e:
            print('process exit wtih code: {}'.format(e.code))
            os._exit(0)
        finally:
            print('clean up...\n')


    #os._exit()不会抛出异常，直接退出进程
    elif choice == '2':
        try:
            os._exit(2) 
        except Exception as e:
            print('process exit with Exception: {}'.format(e))
        finally:
            print('clean up...')
    else:
        print('process continue...')

    #仅在win32平台
    #os.popen, os.system基于subprocess基础实现
    print('os.popen()')
    pipObj = os.popen('python ./.vscode/system_tools/exit_os.py')
    print(pipObj.read(), end = '')
    print(pipObj.close())

    pipObj = os.popen('python ./.vscode/system_tools/exit_sys.py')
    print(pipObj.read(), end = '')
    print(pipObj.close())

    print('\nos.system()')
    exitStat = os.system('python ./.vscode/system_tools/exit_os.py')
    print(exitStat)

    exitStat = os.system('python ./.vscode/system_tools/exit_sys.py')
    print(exitStat)

    print('\nsubprocess.Popen()')
    pipObj = subprocess.Popen('python ./.vscode/system_tools/exit_os.py', stdout=subprocess.PIPE)
    print(pipObj.communicate())
    print(pipObj.returncode)

    pipObj = subprocess.Popen('python ./.vscode/system_tools/exit_sys.py', stdout=subprocess.PIPE)
    print(pipObj.stdout.read())
    pipObj.wait()
    print(pipObj.returncode)

    print('\nsubprocess.call()')
    exitStat = subprocess.call('python ./.vscode/system_tools/exit_os.py')
    print(exitStat)

    exitStat = subprocess.call('python ./.vscode/system_tools/exit_sys.py')
    print(exitStat)