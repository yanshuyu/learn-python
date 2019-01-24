#demo of place geometry manager to arrange widgets
import tkinter

class PlaceGoMgrApp(object):
    def __init__(self):
        self.m_root = tkinter.Tk(screenName='Place Geometry Demo')
    
    def init(self):
        self.m_redLab = tkinter.Label(self.m_root)
        self.m_greenLab = tkinter.Label(self.m_root)
        self.m_blueLab = tkinter.Label(self.m_root)

        self.m_redLab.config(text='Red Lable', background='red')
        self.m_greenLab.config(text='Green Lable', background='green')
        self.m_blueLab.config(text='Bule Lable', background='blue')

        self.m_redLab.place(x=100, y=100)
        self.m_greenLab.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.m_blueLab.place(relx=1, rely=1, x=-100, y=-100, anchor=tkinter.SE)

        self.m_root.geometry('400x400')
        for w in self.m_root.place_slaves():
            print(w['text'], w.place_info())

    def run(self):
        self.m_root.mainloop()


if __name__ == "__main__":
    theApp = PlaceGoMgrApp()
    theApp.init()
    theApp.run()
