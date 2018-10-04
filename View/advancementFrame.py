import ttk
import Tkinter as  tk

class AdvancementFrame():
    def __init__(self, parent, controller, row, isActive):
        self.controller = controller

        self.bonus     = tk.StringVar(value="Choose Bonus")
        self.bonusStat = None
        self.level     = row * 4
        self.isActive  = tk.BooleanVar(value=isActive)

        self.frame = ttk.Frame(parent, padding=10)
        self.frame.grid(row=row, column=0, columnspan=2, padx=10, sticky="NEW")
        self.frame.grid_columnconfigure(1, weight=1)

        tk.Label(self.frame, text=str(self.level)).grid(row=0, column=0, pady=8, padx=10)
        self.menu = tk.OptionMenu(self.frame, self.bonus, *self.controller.ADVANCEMENT)
        self.menu.config(width=25)
        self.menu.grid(row=0, column=1)
        self.menu.config(font=('Helvetica', 10), highlightthickness=0)

        if not self.isActive.get():
            self.menu.config(state="disabled")

        self.controller.char.charLevel.trace("w", lambda i,o,x: self.checkBonusAvailable())
        self.bonus.trace(                    "w", lambda i,o,x: self.updateBonus())


    def checkBonusAvailable(self):
        charLevel = self.controller.char.charLevel.get()

        if charLevel >= self.level:
            if not self.isActive.get():
                self.menu.config(state="normal")
                self.isActive.set(True)
                if self.bonus.get() == "Choose Bonus":
                    self.controller.addAdvancementRequirement(self)
                else:
                    self.updateBonus()
        else:
            if self.isActive.get():
                self.menu.config(state="disable")
                self.isActive.set(False)
                if self.bonusStat is not None:
                    self.controller.controller.removeMod(self.bonus, self.bonusStat)


    def updateBonus(self):
        bonus = self.bonus.get()

        if bonus == "+1 Strength":
            self.bonusStat = "str"
        elif bonus == "+1 Dexterity":
            self.bonusStat = "dex"
        elif bonus == "+1 Constitution":
            self.bonusStat = "con"
        elif bonus == "+1 Intelligence":
            self.bonusStat = "int"
        elif bonus == "+1 Wisdom":
            self.bonusStat = "wis"
        else:
            self.bonusStat = "cha"
        
        self.menu.config(fg="black")
        self.controller.controller.addMod({"target": self.bonusStat, "type": "untyped", "value": 1}, self.bonus, self.menu)