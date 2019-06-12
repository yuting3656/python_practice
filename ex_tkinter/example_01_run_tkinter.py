from tkinter import *

"""
本範例: 如何RUN一個 tkinter 的畫面
文件連結: https://docs.python.org/3/library/tk.html
"""


class TkGui:
    def __init__(self, master):
        self.master = master


if __name__ == "__main__":
    root = Tk()
    app = TkGui(root)
    root.mainloop()
