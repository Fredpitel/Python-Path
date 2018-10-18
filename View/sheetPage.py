import ttk
import Tkinter as tk

class SheetPage:
    def __init__(self, controller, parent):
        self.sheetPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.controller = controller

        # Name
        tk.Label(self.sheetPage, text="Character Name: ").grid(row=0, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.charName).grid(row=0, column=1)
        
        #
        # Attack
        #    
        
        # BAB
        tk.Label(self.sheetPage, text="BAB: ").grid(row=1, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.babString).grid(row=1, column=1)

        # Melee
        tk.Label(self.sheetPage, text="Melee: ").grid(row=2, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.attack.meleeString).grid(row=2, column=1)

        #
        # Saving Throws
        #

        # Fortitude
        tk.Label(self.sheetPage, text="Fortitude: ").grid(row=3, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.fortitude.value).grid(row=3, column=1)

        # Reflex
        tk.Label(self.sheetPage, text="Reflex: ").grid(row=4, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.reflex.value).grid(row=4, column=1)

        # Will
        tk.Label(self.sheetPage, text="Will: ").grid(row=5, column=0)
        tk.Label(self.sheetPage, textvariable=self.controller.char.will.value).grid(row=5, column=1)


        self.sheetPage.update_idletasks()