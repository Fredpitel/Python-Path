import Tkinter as tk

from modifiable import Modifiable

class AbilityScore(Modifiable):
    def __init__(self, char, baseValue, name, shortName):
        Modifiable.__init__(self, char, baseValue)
        self.name      = name
        self.shortName = shortName
        self.bonus     = tk.IntVar(value=0)

        self.value.trace("w", self.updateBonus)


    def updateBonus(self,i,o,x):
        self.bonus.set((self.value.get() - self.char.BASE_ABILITY_VALUE)/2)