import ttk
import tkinter as tk

from tkinter   import *
from classPage import ClassPage
from statsPage import StatsPage
from character import Character

def init():
    root = tk.Tk()
    root.title("Character Sheet")
    root.option_add("*Font", "helvetica 14")

    nb        = ttk.Notebook(root)
    char      = Character()
    classPage = ClassPage(nb, char)
    statsPage = StatsPage(nb, char)

    nb.pack(expand=1, fill="both")

    root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()))
    root.mainloop()

if __name__ == "__main__":
    init()