import fileUtil
import os

if __name__ == '__main__':
    #fileUtil.copyFolder(r'C:\Users\yanshuyu\Desktop\learn-py', r'C:\Users\yanshuyu\Desktop\learn-py\learn-py-copy')
    fileUtil.copyFile(r'D:\Application\xshell\Xshell.exe', r'C:\Users\yanshuyu\Desktop\learn-py\xshell')
    #fileUtil.deleteFolder(r'C:\Users\yanshuyu\Desktop\learn-py\xshell')
    fileUtil.moveFileOrFolder(r'C:\Users\yanshuyu\Desktop\learn-py\xshell', r'D:\Application\xshell\Xshell.exe')