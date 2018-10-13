import ttk
import Tkinter as tk

class SkillPage:
    def __init__(self, controller, parent):
        self.skillPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.controller = controller

        #
        # Skill Table
        #
        skills = self.controller.char.skill.tree.keys()
        skills.sort()
        i = 0
        for skill in skills:
            tk.Label(self.skillPage, text=skill).grid(row=i, column=0)
            i += 1

        tk.Label(self.skillPage, text="Skill Points: ").grid(row=i, column=0)
        tk.Label(self.skillPage, textvariable=self.controller.char.skillPoints.value).grid(row=i, column=1)