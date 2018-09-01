import ttk
import Tkinter as tk

from CreationPage.creationPageController import CreationPageController
from Model.character                     import Character
#from sheetPage                           import SheetPage

class Application(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.nb   = ttk.Notebook(root)
        self.char = Character(self)

        self.creationPageController = CreationPageController(self)
        self.nb.add(self.creationPageController.view.creationPage, text='Character Creation', padding=10)

        #self.sheetPage           = SheetPage(nb, char)

        self.nb.pack(expand=1, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Character Sheet")
    root.option_add("*Font", "helvetica 14")
    root.geometry(str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()))

    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
