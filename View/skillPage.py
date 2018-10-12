import ttk
import Tkinter as tk

class SkillPage:
    def __init__(self, controller, parent):
        self.skillPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.controller = controller

        # Name
        tk.Label(self.skillPage, text="Skill Points: ").grid(row=0, column=0)
        tk.Label(self.skillPage, textvariable=self.controller.char.skillPoints.value).grid(row=0, column=1)