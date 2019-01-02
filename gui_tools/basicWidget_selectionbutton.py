#basic widget check box and radio box demo
import tkinter


def onCheckboxClick(boolVar):
    print(boolVar.get())

def onRadioBtnClick(strVal):
    print(strVal.get())


if __name__ == "__main__":
        root = tkinter.Tk()
        bool_var = tkinter.BooleanVar()
        str_var = tkinter.StringVar(value="no selection")
        
        check_box = tkinter.Checkbutton(root, text='check me')
        check_box.config(variable=bool_var, onvalue=True, offvalue=False, command=lambda : onCheckboxClick(bool_var))
        check_box.pack()

        radio_box_1 = tkinter.Radiobutton(root, text="apple")
        radio_box_2 = tkinter.Radiobutton(root, text="orange")
        radio_box_3 = tkinter.Radiobutton(root, text="banana")
        radio_box_4 = tkinter.Radiobutton(root, text="watermelon")
        radio_box_1.config(variable=str_var, value=radio_box_1["text"], command=lambda : onRadioBtnClick(str_var))
        radio_box_2.config(variable=str_var, value=radio_box_2["text"], command=lambda : onRadioBtnClick(str_var))
        radio_box_3.config(variable=str_var, value=radio_box_3["text"], command=lambda : onRadioBtnClick(str_var))
        radio_box_4.config(variable=str_var, value=radio_box_4["text"], command=lambda : onRadioBtnClick(str_var))
        radio_box_1.pack()
        radio_box_2.pack()
        radio_box_3.pack()
        radio_box_4.pack()

        root.mainloop()