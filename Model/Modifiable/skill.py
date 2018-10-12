import Tkinter as tk

from modifiable import Modifiable

class Skill(Modifiable):
    def __init__(self, baseValue, untrained, penalty, stat):
        Modifiable.__init__(self, baseValue)

        self.untrained  = untrained
        self.penalty    = penalty
        self.stat       = stat
        self.classSkill = tk.BooleanVar(value=False)

        self.classSkill.trace("w", lambda i,o,x: self.updateClassSkill())


    def updateClassSkill(self):
        if self.classSkill.get():
            self.addModifier({"target": self.stat, "type": "class", "value": 3}, self.classSkill)