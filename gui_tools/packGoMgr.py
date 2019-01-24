#demo of using pack geometry manager to arrage widget
import tkinter
from tkinter import ttk

COLORS = {
    "Red":"#ff0000",
    "Green":"#00ff00",
    "Blue":"#0000ff",
    "Grey":"#888888",
    "Yellow":"#ffff00",
}

if __name__ == "__main__":
    root = tkinter.Tk()

    lab_red = tkinter.Label(root)
    lab_green = tkinter.Label(root)
    lab_blue = tkinter.Label(root)

    lab_red.config(text="Red Lable", bg=COLORS["Red"], activeforeground=COLORS["Yellow"])
    lab_green.config(text="Green Lable", bg=COLORS["Green"], activeforeground=COLORS["Yellow"])
    lab_blue.config(text="Blue Lable", bg=COLORS["Blue"], activeforeground=COLORS["Yellow"])

    lab_red.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    lab_green.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    lab_blue.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

    for child in root.pack_slaves():
        print(child)
        print(" ", child.pack_info())

    root.mainloop()
