from modifiable import Modifiable

class SkillPoints(Modifiable):
    def __init__(self, baseValue, char):
        Modifiable.__init__(self, baseValue)
        self.char = char
        
        self.char.int.bonus.trace(   "w", lambda i,o,x: self.updateBaseValue())
        self.char.spFromLevels.trace("w", lambda i,o,x: self.updateBaseValue())
        self.char.race.trace        ("w", lambda i,o,x: self.updateBaseValue())


    def updateBaseValue(self):
        baseSP = self.char.charLevel.get() * self.char.int.bonus.get()
        baseSP += self.char.spFromLevels.get()

        if self.char.race.get() == "Human":
            baseSP += 1 * self.char.charLevel.get()

        self.baseValue.set(baseSP)