import os
import shutil

#拷贝源文件夹到目标文件夹
def copyFolder(scrFolder, dstFolder, force=True):
    if not os.path.isdir(scrFolder):
        print('scrFolder must be a floder!')
        return False
    if not os.path.isdir(dstFolder):
        print('scrFolder must be a floder!')
        return False       
    try:
        if os.access(dstFolder, os.F_OK):
            if force:
                shutil.rmtree(dstFolder)
            else:
                print('copy failed! ' + dstFolder + 'is already exited.')
                return False            
        shutil.copytree(scrFolder, dstFolder)

    except Exception as e:
        print('copy failed! error:', e)
        return False
    else:
        return True


#拷贝源文件到目标文件或目标文件夹
def copyFile(scrFile, dst):
    if os.path.isdir(scrFile):
        print(scrFile + 'is a directory, not a file!')
        return False
    try:
        _ , ext = os.path.splitext(dst)
        floder_name = os.path.dirname(dst) if ext else dst
        if not os.access(floder_name, os.F_OK):
            createFolder(floder_name) 
        shutil.copy2(scrFile, dst)
    except Exception as e:
        print('copy faild! error:', e)    
        return False

    return True


#创建文件夹
def createFolder(dstFolder, recursive=True):
    if os.path.isfile(dstFolder):
        print(dstFolder + 'is not a floder!')
        return False
    if os.access(dstFolder, os.F_OK):
        return True
    if not os.access(os.path.dirname(dstFolder), os.F_OK) and not recursive:
        return False
    os.makedirs(dstFolder, exist_ok=True)

    return True


#删除文件夹
def deleteFolder(targetFolder):
    if os.path.isfile(targetFolder):
        print(targetFolder + 'is not a vailed folder!')
        return False
    try:
        shutil.rmtree(targetFolder)
    except Exception as e:
        print('delete folder failed! error: ', e)
        return False
   
    return True


#移动文件\文件夹
def moveFileOrFolder(scr, dstFolder):
    _, ext = os.path.splitext(dstFolder)
    if ext:
        print(dstFolder + 'is not a vailed folder!')
        return False
    try:
        shutil.move(scr, dstFolder)
    except Exception as e:
        print('move failed! error: ', e)
        return False
    
    return True