from tkinter import *
from tkinter import ttk


"""
本範例: tkinter 
文件連結:
"""


class Cool_Gui:
    def __init__(self, master):
        self.master = master
        self._create_gui()

    def _create_gui(self):
        self.master.configure(background='#3CB371')
        # 視窗大小
        self.master.geometry("500x400")


if __name__ == "__main__":
    root = Tk()
    Cool_Gui(root)
    root.mainloop()
