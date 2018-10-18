from math       import floor
from modifiable import Modifiable

class Will(Modifiable):
    def __init__(self, baseValue, char):
        Modifiable.__init__(self, baseValue)
        self.char = char

        self.char.wis.bonus.trace("w", lambda i,o,x: self.updateBaseValue())


    def updateBaseValue(self):
        will = 0

        for className in self.char.charClass:
            charClass = self.char.charClass[className]

            if charClass.willProg == 2:
                will += charClass.willProg + (charClass.nbLevels/2)
            else:
                will += charClass.willProg + (charClass.nbLevels/3)

        will = int(floor(will)) + self.char.wis.bonus.get()

        self.baseValue.set(will)