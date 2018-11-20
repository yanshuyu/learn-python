import multiprocessing
import os
import time

def who(msg,lck):
    with lck:
        print('process id: %d   message:%s'%(os.getpid(), msg))


def doSomeTask(p):
    print('child process %s is start.'%(os.getpid()))
    time.sleep(5)
    p.send(['hello world', 3.14159, 'some result'])
    reply = p.recv()
    print('child process %s revc: '%(os.getpid()), reply)
    print('child process %s is exit.'%(os.getpid()))


def modifySomeShareMemory(log, val, arr):
    print(log)
    val.value += 1
    for i in range(4):
        arr[i] += 1
    global g_counter
    g_counter += 1


g_counter = 0

if __name__ == '__main__':
    lck = multiprocessing.Lock()

    print('parent process start.')
    who('this is parent prcess', lck)

    #spawn new task running in independent process
    childProc = []
    for i in range(5):
        c = multiprocessing.Process(target=who, args=('this is  child process %d'%(i), lck))
        c.start()
        childProc.append(c)

    for c in childProc:
        c.join()

    with lck:
        print('parent process exit.')

    print('\n\n\n')
    #ipc tools
    #pipe in multiprocessing
    print('parent process %s is start.'%(os.getpid()))
    parentEnd, childEnd = multiprocessing.Pipe()
    childProc = multiprocessing.Process(target=doSomeTask, args=(childEnd,))
    childProc.start()
    reply = parentEnd.recv()
    print('parent process %s revice: '%(os.getpid()), reply)
    time.sleep(3)
    parentEnd.send(['hello from parent', 456416] + reply)
    childProc.join()
    print('parent process %s is exit.'%(os.getpid()))


    #share memory, value array, thread and process safe
    shareVal = multiprocessing.Value('i', 0)
    shareArr = multiprocessing.Array('i', 4)
    
    print('\n\n\n')
    print('parent process %s is start.'%(os.getpid()))
    modifySomeShareMemory('modify form parent process: %d'%(os.getpid()), shareVal, shareArr)
    print('g_couter: ', g_counter)
    print('share val', shareVal.value)
    print('share arr', list(shareArr))

    childProc = []
    for i in range(4):
        proc = multiprocessing.Process(target=modifySomeShareMemory, args=('modify from child process: %d'%(i), shareVal, shareArr))
        proc.start()
        childProc.append(proc)
        
    for p in childProc:
        p.join()

    print('g_couter: ', g_counter)
    print('share val', shareVal.value)
    print('share arr', list(shareArr))
    print('parent process %s is exit.'%(os.getpid()))
