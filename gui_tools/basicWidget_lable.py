#demo of using lable widget
import tkinter
import os

if __name__ == "__main__":
    root = tkinter.Tk()
    lable = tkinter.Label(root)

    #display text
    fpath = os.path.join(os.getcwd(), 'gui_tools','basicWidget_lable.py')
    print('file path: ', fpath)
    f = open(fpath, mode='rt', encoding='utf8')
    lines = f.readlines()
    content = ''
    for line in lines:
        content += line
    print('file content: ', content)
    lable.config(text=content)

    #display image
    imgpath = os.path.join(os.getcwd(), 'gui_tools', 'pylogo.png')
    logobitmap = tkinter.PhotoImage(file=imgpath)
    print('logobitmap: ', logobitmap)
    lable.config(image=logobitmap, compound='right')
    
    
    lable.pack(expand=False, fill=tkinter.NONE, side=tkinter.TOP,)

    print('all config properties: ')
    for k, v in lable.config().items():
        print(k, '=', v)

    root.mainloop()