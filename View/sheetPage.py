import ttk
import Tkinter as tk

class SheetPage:
    def __init__(self, controller, parent):
        self.sheetPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.controller = controller

        # Name
        tk.Label(self.sheetPage, text="Character Name: ").grid(row=0, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.charName).grid(row=0, column=1)