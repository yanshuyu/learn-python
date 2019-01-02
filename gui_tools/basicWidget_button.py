#tk button basic widget demo
import os
import tkinter


def onBtnOkClik():
    print('ok')

def onBtnCancelClick():
    print('cancel')

if __name__ == "__main__":
    root = tkinter.Tk()
    btn = tkinter.Label(root, text='this is a tk basic button widget demo')
    btn.pack()

    btn_ok = tkinter.Button(root, text='ok(确认)')
    btn_cancel = tkinter.Button(root, text='cancel(取消)')

    image_ok_path = os.path.join(os.getcwd(), 'gui_tools', 'btn_orange_164x89_l25_r25_t25_b25.png')
    image_cancel_path = os.path.join(os.getcwd(), 'gui_tools', 'btn_hui.png')
    ok_image = tkinter.PhotoImage(file=image_ok_path)
    cancel_image = tkinter.PhotoImage(file=image_cancel_path)

    btn_ok.config(image=ok_image, compound=tkinter.CENTER, command=onBtnOkClik)
    btn_cancel.config(image=cancel_image, compound=tkinter.CENTER, command=onBtnCancelClick)

    btn_ok.pack(side=tkinter.LEFT)
    btn_cancel.pack(side=tkinter.RIGHT)

    root.mainloop()