import ttk
import Tkinter as tk


class SkillWindow:
    def __init__(self, controller, list, frame):
        self.controller = controller
        skillWindow = tk.Toplevel()
        skillWindow.title("Add Skill")

        innerframe = ttk.Frame(skillWindow, relief=tk.RAISED, padding=10)
        innerframe.pack()
        tk.Label(innerframe, text="Choose skill(s) to add").grid(row=0, column=0, columnspan=2, sticky="EW")
        
        checkboxes = []

        i=1
        for skill in list:
            label = tk.Label(innerframe, text=skill)
            label.config(font=('Helvetica', 10))
            label.grid(row=i, column=0)

            var = tk.IntVar()
            checkbox = tk.Checkbutton(innerframe, variable=var)
            checkbox.grid(row=i, column=1)
            checkbox.skill = skill
            checkbox.var   = var

            checkboxes.append(checkbox)

            i+=1

        self.addButton = tk.Button(innerframe, text="Add", command=lambda c=checkboxes, f=frame: self.controller.addSkill(skillWindow,c,f))
        self.addButton.grid(row=i, column=0, columnspan=2, pady=10)