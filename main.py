import ttk
import Tkinter as tk

from Controller.characterController import CharacterController
from splash import Splash

class Application(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Character", command=self.createNewCharacter)
        filemenu.add_command(label="Open File")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        self.splash = Splash()

        self.nb = ttk.Notebook(root)
        self.nb.grid(row=0, column=0, sticky="NSEW")

        self.createNewCharacter()

        self.splash.destroy()


    def createNewCharacter(self):
        controller = CharacterController(self.nb)
        controller.char.charName.trace("w", lambda i,o,x, name=controller.char.charName: self.changeTabText(name))
        self.nb.add(controller.view, text="New Character", padding=5)


    def changeTabText(self, name):
        self.nb.tab(self.nb.select(), text=name.get())


if __name__ == "__main__":
    root = tk.Tk()

    root.attributes("-zoomed", True)
    root.title("Character Sheet")
    root.option_add("*Font", "helvetica 14")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    mainApp = Application(root)
    mainApp.grid(row=0, column=0, sticky="NSEW")

    root.mainloop()