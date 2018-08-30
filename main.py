import ttk
import tkinter as tk

from CreationPage import *
from statsPage    import *
from character    import *

def init():
    root = tk.Tk()
    root.title("Character Sheet")
    root.option_add("*Font", "helvetica 14")

    nb   = ttk.Notebook(root)
    char = Character()

    creationPageController = CreationPageController(char, nb)
    nb.add(creationPageController.view.creationPage, text='Character Creation', padding=10)

    statsPage           = StatsPage(nb, char)

    nb.pack(expand=1, fill="both")

    root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()))
    root.mainloop()

if __name__ == "__main__":
    init()