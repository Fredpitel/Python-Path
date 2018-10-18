from math       import floor
from modifiable import Modifiable

class Fortitude(Modifiable):
    def __init__(self, baseValue, char):
        Modifiable.__init__(self, baseValue)
        self.char = char

        self.char.con.bonus.trace("w", lambda i,o,x: self.updateBaseValue())


    def updateBaseValue(self):
        fort = 0

        for className in self.char.charClass:
            charClass = self.char.charClass[className]

            if charClass.fortProg == 2:
                fort += charClass.fortProg + (charClass.nbLevels/2)
            else:
                fort += charClass.fortProg + (charClass.nbLevels/3)

        fort = int(floor(fort)) + self.char.con.bonus.get()

        self.baseValue.set(fort)