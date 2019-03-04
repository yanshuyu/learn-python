#python variable search scope
#<1> enclose functions.
#<2> local 
#<3> global(module)
#<4> build in

#global
pi = 3.14

def foo():
    #local 
    pi = 3.14159
    def goo():
        print('pi in goo: ', pi)
    goo()
    print('pi in foo: ', pi)
    pi = 6.28

def changeGlobal():
    global pi
    pi = 6.28

print('before call foo, pi: ', pi)
foo()
print('after call foo, pi: ', pi)
changeGlobal()
print('after call changeGlobal, pi', pi)