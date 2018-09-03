import Tkinter as tk

from modifiable import Modifiable

class AbilityScore(Modifiable):
    BASE_ABILITY_VALUE = 10
    
    def __init__(self, baseValue, name, shortName):
        Modifiable.__init__(self, baseValue)
        self.name      = name
        self.shortName = shortName
        self.bonus     = tk.IntVar(value=0)


    def update(self):
        self.bonus.set((self.value.get() - self.BASE_ABILITY_VALUE)/2)
        super(AbilityScore, self).update()