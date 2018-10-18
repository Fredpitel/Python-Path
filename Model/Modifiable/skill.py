import Tkinter as tk

from modifiable import Modifiable

class Skill(Modifiable):
    def __init__(self, data, controller):
        Modifiable.__init__(self, 0)
        self.controller = controller

        self.untrained  = data["untrained"]
        self.penalty    = data["penalty"]
        self.statName   = data["stat"]
        self.bonus      = self.controller.getTarget(self.statName).bonus
        self.classSkill = tk.BooleanVar(value=False)
        self.rank       = tk.IntVar(value=0)

        self.modAdded   = False

        self.classSkill.trace("w", lambda i,o,x: self.updateClassSkill())
        self.rank.trace(      "w", lambda i,o,x: self.update())
        self.bonus.trace(     "w", lambda i,o,x: self.update())


    def updateClassSkill(self):
        if self.classSkill.get() and self.rank.get() > 0 and not self.modAdded:
            self.modAdded = True
            self.addModifier({"target": self, "type": "class", "value": 3}, self.classSkill)
        else:
            self.modAdded = False


    def update(self):
        total = 0

        total += self.rank.get()
        total += self.bonus.get()

        if self.classSkill.get() and not self.modAdded:
            self.updateClassSkill()
        elif self.modAdded and self.rank.get() == 0:
            self.modAdded = False
            self.removeModifier(self.classSkill)

        self.baseValue.set(total)
        super(Skill, self).update()