
class customInputObject:
    def __init__(self, text = ''):
        self.m_ibuffer = text

    def read(self, sz = None):
        if sz == None or sz > len(self.m_ibuffer):
            sz = len(self.m_ibuffer)
        rpart, self.m_ibuffer = self.m_ibuffer[:sz], self.m_ibuffer[sz:]
        return rpart

    
    def readline(self, sz = None):
        pos = self.m_ibuffer.find('\n')
        rpart, self.m_ibuffer = self.m_ibuffer[:pos], self.m_ibuffer[pos+1:]
        return rpart

    def readlines(self, hint = None):
        lines = self.m_ibuffer.splitlines()
        self.m_ibuffer = ''
        return lines
    

class customOutputObject:
    def __init__(self):
        self.m_obuffer = ''
    
    def write(self, text):
        self.m_obuffer += text
        return len(text)

    def writelines(self, lines):
        for line in lines:
            self.write(line)


def ioredirect(func, kargs, inputStr = ''):
    import sys
    #save old std i/o stream objet
    i_old, o_old = sys.stdin, sys.stdout

    #assign new i/o object
    sys.stdin = customInputObject(inputStr)
    sys.stdout = customOutputObject()
    try:
        result = func(**kargs)
        output = sys.stdout.m_obuffer
    finally:
        sys.stdin, sys.stdout = i_old, o_old
    
    return result, output




        