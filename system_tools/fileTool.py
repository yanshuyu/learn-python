import os
import sys


def fileScanner(fname, func, encode):
    return [func(line)  for line in open(fname, 'r', encoding=encode)]

if __name__ == '__main__':
    # text mode file encoding
    # f = open(fileName, mode, encoding='utf8')
    # f.write('xxx')
    #     |          utf8 encoding                 save to external file
    #     | 'xxx'--------------------> b'yyy' -----------------------------> fileName
    #     |
    # f = open(fileName, mode, encoding='utf8')
    # f.read()
    #     |           utf8 decoding
    #     | b'yyy'-------------------> 'xxx'
    utf8File = open('data-utf8.txt', 'wt', encoding='utf8')
    try:
        utf8File.write('<xml>\n')
        utf8File.write('text=hello world\n')
        utf8File.write('text=你好 世界\n')
        utf8File.write('</xml>\n')
    finally:
        utf8File.close()
    

    #open with text mode, default encoding(not utf8)
    utf8File = open('data-utf8.txt')
    try:
        # for line in utf8File.readlines():
        #     print(line, end='')

        # print()

        # utf8File.seek(0)
        print('utf8 text data: ', end='')
        for line in utf8File:
            print(line, end='')
        print()
    finally:
        utf8File.close()
    


    utf16File = open('data-utf16.txt', 'w', encoding='utf16')
    try:
        utf16File.write('<xml>\n')
        utf16File.write('text=hello world\n')
        utf16File.write('text=你好 世界\n')
        utf16File.write('</xml>\n')
    finally:
        utf16File.close()
    utf16File = open('data-utf16.txt', 'r', encoding='utf16')
    try:
        print('utf16 text data: ', end='')
        for line in utf16File:
            print(line, end='')
        print()
    finally:
        utf16File.close()

    #dump utf8, utf16 encoding file binary data
    utf8File = open('data-utf8.txt', 'rb')
    utf16File = open('data-utf16.txt', 'rb')
    print('utf8 binary data: ', utf8File.read())
    print('utf16 binary data: ', utf16File.read())
    utf8File.seek(0)
    bytesString = utf8File.read()
    bytesString = utf8File.read()
    print(type(bytesString))
    #print(help(bytes))
    
    utf8File.close()
    utf16File.close()
    print()

    # os module files tool
    fd = os.open('data-utf8.txt', os.O_BINARY | os.O_RDONLY)
    print('file descriptor: ', fd)
    print('8 bytes of content: ', os.read(fd, 8))
    print('another 8 bytes content: ', os.read(fd, 8))
    os.lseek(fd, 0, 0)
    print('100 bytes content: ', os.read(fd, 100))
    print()

    fObject = os.fdopen(fd, 'r', encoding='utf8')
    fObject.seek(0)
    print(fObject.read())
    fObject.close()

    # std stream fd
    stdStream = (sys.stdin, sys.stdout, sys.stderr)
    print('std stream fds:')
    for s in stdStream:
        print(s.fileno())
    print('this is a test std error msg', file=sys.stderr)
    os.write(sys.stderr.fileno(), b'this is another test std error msg.\n')

    # file permission
    os.chmod('data-utf8.txt',   0o600)
    #os.rename('data-utf8.txt', 'data-utf8-copy.txt')
    #os.remove('data-utf8.txt')
    st = os.stat('data-utf8.txt')
    print(st)
    print(os.path.isdir('data-utf8.txt') ,os.path.isfile('data-utf8.txt') ,os.path.getsize('data-utf8.txt'))

    lines =  fileScanner('data-utf8.txt', lambda l : l.upper(), 'utf8')
    for l in lines:
        print(l)


    