import os
import _thread
import threading
from time import sleep


Jobs_Cnt = 6
Cnt_Num = 10
stdout_lock = _thread.allocate_lock()
job_done_flag = [False for i in range(Jobs_Cnt)]

def doSomeCounting(id, cnt):
    for x in range(1, cnt+1):
        print('thread {} counting: {}'.format(id, x))
        sleep(1)

def doSomeCountingSync(id, cnt):
    for x in range(1, cnt+1):
        stdout_lock.acquire()
        print('thread {} counting: {}'.format(id, x))
        stdout_lock.release()
        sleep(1)


def doSomeCountingSyncAndWait(id, cnt):
    for x in range(1, cnt+1):
        stdout_lock.acquire()
        print('thread {} counting: {}'.format(id, x))
        
        if x == cnt:
            job_done_flag[id-1] = True
         
        stdout_lock.release()
        sleep(1)


job_done_mut = [ _thread.allocate_lock() for i in range(Jobs_Cnt)]
def doSomeCountingSyncAndWaitNoBusyLoopExceptionSafe(id, cnt, mut):
    for i in range(1, cnt+1):
        sleep(1/(id+1))
        with mut: #auto acquire / release, with
            print('thread {} countint: {}'.format(id, i))
    job_done_mut[id].acquire()



class countingThread(threading.Thread):
    def __init__(self, id, cnt, mut):
        threading.Thread.__init__(self)
        self.m_id = id
        self.m_cnt = cnt
        self.m_mut = mut

    def run(self):
        for i in range(1, self.m_cnt+1):
            with self.m_mut:
                sleep(0.1)
                print('thread {} counting: {}'.format(self.m_id, i))
        


if __name__ == '__main__':
    #multi thread without sync
    # for j in range(Jobs_Cnt+1):
    #     _thread.start_new_thread(doSomeCounting, (j,Cnt_Num))
    # doSomeCounting(Jobs_Cnt, Cnt_Num)


    #multi thread without sync
    # for j in range(1,Jobs_Cnt):
    #     _thread.start_new_thread(doSomeCountingSync, (j,Cnt_Num)) 
    # doSomeCountingSync(Jobs_Cnt, Cnt_Num)


    #waiting for child threads(busy loop, no exception safe)
    # print('job done: {}'.format(job_done_flag))
    # for j in range(1,Jobs_Cnt):
    #     _thread.start_new_thread(doSomeCountingSyncAndWait, (j,Cnt_Num)) 
    # doSomeCountingSyncAndWait(Jobs_Cnt, Cnt_Num)
    # for flag in job_done_flag:
    #     while not flag:
    #         pass
    # print('job done: {}'.format(job_done_flag))

    #sync
    #wait(no busy loop)
    #exception safe
    print('main thread start.')
    for i in range(Jobs_Cnt):
        _thread.start_new_thread(doSomeCountingSyncAndWaitNoBusyLoopExceptionSafe, (i, Cnt_Num, stdout_lock))
    for mut in job_done_mut:
        while not mut.locked():
            sleep(0.1)
    print()
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    print()

    #the threading module
    #object base thread model
    countingMut = threading.Lock()
    countingThreads = [ countingThread(i, Cnt_Num, countingMut) for i in range(Jobs_Cnt)]
    for t in countingThreads:
        t.start()
    for t in countingThreads:
        t.join()
    print()
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    print()

    
    countingThreads = [ threading.Thread(target=doSomeCountingSync, args=(i,Cnt_Num))  for i in range(Jobs_Cnt)]
    for t in countingThreads:
        t.start()
    for t in countingThreads:
        t.join()
    print('main thread exit.')