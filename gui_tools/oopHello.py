# oop hello world tk demo
# use grid geometry manager to pack widgets
import tkinter

class helloApp:
    def __init__(self, pWidget):
        self.m_parent = pWidget
        self.m_lable = tkinter.Label(self.m_parent, text='press button(点击按钮)')
        self.m_lable.grid(row=0, column=0, columnspan=2)
        tkinter.Button(self.m_parent, text='English', command=self.onBtnEngClick).grid(row=1, column=0)
        tkinter.Button(self.m_parent, text='中文', command=self.onBtnChcnClick).grid(row=1, column=1)

    def onBtnEngClick(self):
        self.m_lable['text'] = 'hello tkinter Gui!'

    def onBtnChcnClick(self):
        self.m_lable['text'] = '你好 tkinter用户图形界面!'

def main():
    root = tkinter.Tk()
    helloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()