#inter-process communication ：
# Program exit status codes
# Shell environment variables
# Standard stream redirections
# Stream pipes(anonymous pipes, named pipes)
# Sockets

# using un-named pipe with threads
# os.fork() is not avalible in win-32
import os
import threading
import time
import socket
import threading


def msgProducer(pw):
    for i in range(1,10):
        time.sleep(2)
        msg = '[thread %d] this is some message.\n'%(threading.get_ident())
        os.write(pw, msg.encode())
    q_sig = '[thread %d] q \n'%(threading.get_ident())
    os.write(pw, q_sig.encode())


def msgComsumer(pr):
    reader = os.fdopen(pr)
    while True:
        msg = reader.readline()
        if 'q' in msg or 'quit' in msg or 'exit' in msg:
            break
        print('[thread %d] got msg: %s'%(threading.get_ident(), msg))



LOCAL_HOST = 'localhost'
SERVER_JOB_PORT = 50004
MAX_CONNECT_CNT = 5
STDOUT_LCK = threading.Lock()
# using socket with process or threads
def serverJob(lck):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(LOCAL_HOST, SERVER_JOB_PORT)
    s.listen(MAX_CONNECT_CNT)
    cons = []
    conCnt = 0
    while True:
        cli_con,  cli_host= s.accept()
        data = cli_con.recv(1024)
        with lck:
            print('server revice data form {}: {}'.format(cli_host, data))
        replyData = 'hello {}, you send me with data: {}'.format(cli_host, data)
        cli_con.send(replyData.encode)
        cons.append(cli_con)
        conCnt += 1
        if conCnt >= MAX_CONNECT_CNT:
            break
        
    for con in cons:
        con.close()


def clientJob(lck):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.connect((LOCAL_HOST, SERVER_JOB_PORT))
        data = 'client{}: hello，你好'.format(i)
        s.send(data.encode())
        replyData = s.recv(1024)
        with lck:
            print('client{} revice reply form server with data: {}'.format(i, replyData))


if __name__ == '__main__':
    #pipe
    # pReader, pWriter = os.pipe()
    # t_producer  = threading.Thread(target=msgProducer, args=(pWriter,))
    # t_producer.start()
    # msgComsumer(pReader)
    # t_producer.join()


    #socket
    t_svrver = threading.Thread(target=serverJob, args=(STDOUT_LCK,))
    t_svrver.start()

    clients = []
    for i in range(MAX_CONNECT_CNT):
        t_client = threading.Thread(target=clientJob, args=(STDOUT_LCK,))
        t_client.start()
        clients.append(t_client)

    t_svrver.join()    
    for c in clients:
        c.join()

    



