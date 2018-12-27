import tkinter


if __name__ == "__main__":
    # frame01
    # lable = tkinter.Label(None, text="你好Tkinter")
    # lable.pack()
    # lable.mainloop()

    #frame02
    mainWnd = tkinter.Tk()
    lable = tkinter.Label(mainWnd,text='hello Tk!')
    lable.pack()

    print(lable['text'])
    lable['text'] = 'hello python!'
    print(lable.config())

    mainWnd.mainloop()
   
   #frame03
   #tkinter._test()