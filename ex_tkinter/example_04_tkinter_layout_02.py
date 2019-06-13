from tkinter import *
from tkinter import ttk

"""
本範例: tkinter layout 2
相關文件: https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
"""


class DdpGUI:
    def __init__(self, master):
        self.master = master
        self._create_gui()

    def _create_gui(self):
        self.master.configure(background='bisque')
        self.style_frame_bg = ttk.Style()

        self.style_frame_bg.configure('Sample.eye.TFrame', background='black')
        self.style_frame_bg.configure('Sample.pupil.TFrame', background='#f4f4f4')
        self.style_frame_bg.configure('Sample.teeth.TFrame', background='red')

        self.master.geometry("500x400")

        # 相關連結: https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
        self.master.rowconfigure(0, weight=3)
        self.master.rowconfigure(1, weight=3)
        self.master.rowconfigure(2, weight=3)
        self.master.rowconfigure(3, weight=3)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.master.columnconfigure(6, weight=1)
        self.master.columnconfigure(7, weight=1)

        self.frame_01 = ttk.Frame(self.master, style='Sample.eye.TFrame')
        self.frame_01.grid(row=1, column=2, sticky='nsew')
        self.pupil_frame_01 = ttk.Frame(self.frame_01, style='Sample.pupil.TFrame')
        self.pupil_frame_01.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame_02 = ttk.Frame(self.master, style='Sample.eye.TFrame')
        self.frame_02.grid(row=1, column=5, sticky='nsew')
        self.pupil_frame_01 = ttk.Frame(self.frame_02, style='Sample.pupil.TFrame')
        self.pupil_frame_01.pack(fill="both", expand=True, padx=10, pady=10)

        self.frame_03 = ttk.Frame(self.master, style='Sample.teeth.TFrame')
        self.frame_03.grid(row=3, column=2, sticky='nsew')

        self.frame_04 = ttk.Frame(self.master, style='Sample.teeth.TFrame')
        self.frame_04.grid(row=4, column=3, columnspan=3, sticky='nsew')

        self.frame_04 = ttk.Frame(self.master, style='Sample.teeth.TFrame')
        self.frame_04.grid(row=3, column=6, sticky='nsew')


if __name__ == "__main__":
    root = Tk()
    DdpGUI(root)
    root.mainloop()
