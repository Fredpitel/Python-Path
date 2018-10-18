import Tkinter as tk

from math       import floor
from modifiable import Modifiable


class Attack(Modifiable):
    def __init__(self, baseValue, char):
        Modifiable.__init__(self, baseValue)
        self.char = char
        self.meleeString = tk.StringVar()

        self.char.str.bonus.trace("w", lambda i,o,x: self.updateBaseValue())


    def updateBaseValue(self):
        bab = self.char.getBab()
        melee = bab + self.char.str.bonus.get() 
        self.baseValue.set(melee)

        nbAttack = int(floor(bab / 6)) + 1
        attackString = ""

        for i in range(0, int(nbAttack)):
            meleeValue = "+" + str(melee) if melee > 0 else str(melee)
            attackString = attackString + str(meleeValue) + "/"
            melee -= 5

        self.meleeString.set(attackString[:-1])