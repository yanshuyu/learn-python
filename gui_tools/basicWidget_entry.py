#basic widget entry demo
import tkinter

def onOkBtnClick(input_filed):
    print(input_filed.get())

def onClearBtnClick(input_filed):
    input_filed.delete(0, tkinter.END)



if __name__ == "__main__":
    root = tkinter.Tk()

    input_filed = tkinter.Entry(root, width=30)
    input_filed.pack()

    ok_btn = tkinter.Button(root)
    ok_btn.config(text='ok', command=lambda : onOkBtnClick(input_filed))
    ok_btn.pack(side=tkinter.LEFT)

    clear_btn = tkinter.Button(root)
    clear_btn.config(text='clear', command=lambda : onClearBtnClick(input_filed))
    clear_btn.pack(side=tkinter.RIGHT)

    root.mainloop()

