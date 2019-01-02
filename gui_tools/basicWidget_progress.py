#basic widget progressbar and scale demo
import tkinter
from tkinter import ttk

def onBtnAStartClick(progress_a):
    progress_a.start()

def onBtnAStopClick(progress_a):
    progress_a.stop()

if __name__ == "__main__":
    root = tkinter.Tk()

    double_var = tkinter.DoubleVar(0)

    progress_a = ttk.Progressbar(root)
    progress_a.config(length=150, orient=tkinter.HORIZONTAL, mode='indeterminate')
    progress_a.grid(row=0, column=0)

    btn_a_start = ttk.Button(root)
    btn_a_start.config(text='start', command=lambda : onBtnAStartClick(progress_a))
    btn_a_start.grid(row=0, column=1)

    btn_a_stop = ttk.Button(root)
    btn_a_stop.config(text='stop', command=lambda : onBtnAStopClick(progress_a))
    btn_a_stop.grid(row=0, column=2)

    progress_b = ttk.Progressbar(root)
    progress_b.config(length=150, orien=tkinter.HORIZONTAL, mode='determinate', maximum=10, variable=double_var)
    progress_b.grid(row=1, column=0)


    slider = ttk.Scale(root)
    slider.config(from_=0, to=10, length=150, variable=double_var)
    slider.grid(row=1, column=1, padx=10)

    for k, v in progress_b.config().items():
        print(k, ' = ', v)

    print('\n\n')

    for k, v in slider.config().items():
        print(k, ' = ', v)


    root.mainloop()