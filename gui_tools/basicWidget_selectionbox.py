#baic widget demo of combobox and spinbox
import tkinter

def onSpinBoxEvent(intVar):
    print(intVar.get())

if __name__ == "__main__":
    root = tkinter.Tk()
    int_var = tkinter.IntVar(value=0)
    spin_box = tkinter.Spinbox(root)
    spin_box.config(from_=1900, to=2018, textvariable=int_var, command=lambda : onSpinBoxEvent(int_var))
    int_var.set(2018)

    spin_box.pack()
    root.mainloop()
    