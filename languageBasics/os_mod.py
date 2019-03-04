import os

print(os.name)
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.pathsep)
print(os.linesep)
print(os.defpath)
os.system('dir .')
print(os.popen('dir .').read())
print(help(os))
