from tkinter import *
from tkinter import ttk

"""
本範例: tkinter 基本使用
文件連結: https://docs.python.org/3/library/tk.html
"""


class TkGui:
    def __init__(self, master):
        self.master = master
        self.master.title("視窗標題")

        self.frame = ttk.Frame(self.master)
        self.frame.pack()
        # Button 1
        self.hi_there = Button(self.frame)
        # Button 2
        self.quit = Button(self.frame, text="QUIT", fg="red",
                           command=self.master.destroy)

        self.create_widgets()

    def create_widgets(self):
        # Button 1
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        # Button 2
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == "__main__":
    root = Tk()
    app = TkGui(root)
    root.mainloop()
