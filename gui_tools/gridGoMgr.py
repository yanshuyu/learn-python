#demo of using grid geometry to arrange widgets
import tkinter
from tkinter import ttk

class GridGoMgrApp(object):
    def __init__(self):
        self.m_root = tkinter.Tk()
    
    def init(self):
        self.m_navLab = tkinter.Label(self.m_root)
        self.m_wsLab = tkinter.Label(self.m_root)
        self.m_resLab = tkinter.Label(self.m_root)
        
        self.m_navLab.config(text="Navigation Area", background='green')
        self.m_navLab.grid(row=0, column=0, rowspan=2, sticky=tkinter.NSEW)

        self.m_wsLab.config(text="Working Space Area", background='blue')
        self.m_wsLab.grid(row=0, column=1,  sticky=tkinter.NSEW)

        self.m_resLab.config(text="Resource Area", background='red')
        self.m_resLab.grid(row=1, column=1, sticky=tkinter.NSEW)

        self.m_root.grid_rowconfigure(index=0, weight=3)
        self.m_root.grid_rowconfigure(index=1, weight=1)
        self.m_root.grid_columnconfigure(index=0, weight=1)
        self.m_root.grid_columnconfigure(index=1, weight=4)

    def run(self):
        self.m_root.mainloop()
    

if __name__ == "__main__":
    theApp = GridGoMgrApp()
    theApp.init()
    theApp.run()
    



