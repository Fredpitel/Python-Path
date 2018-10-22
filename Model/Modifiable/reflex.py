from math       import floor
from modifiable import Modifiable

class Reflex(Modifiable):
    def __init__(self, baseValue, char):
        Modifiable.__init__(self, baseValue)
        self.char = char

        self.char.dex.bonus.trace("w", lambda i,o,x: self.updateBaseValue())


    def updateBaseValue(self):
        ref = 0

        for className in self.char.charClass:
            charClass = self.char.charClass[className]

            if charClass.refProg == 2:
                ref += charClass.refProg + (charClass.nbLevels.get()/2)
            else:
                ref += charClass.refProg + (charClass.nbLevels.get()/3)

        ref = int(floor(ref)) + self.char.dex.bonus.get()

        self.baseValue.set(ref)