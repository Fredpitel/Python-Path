class Level:
    def __init__(self, charClass, hpVar):
        self.charClass = charClass
        self.hpVar = hpVar
        self.hpGained = hpVar.get()
        self.hpVar.trace("w", self.updateHpGained)

    def updateHpGained(self,i,o,x):
        self.hpGained = self.hpVar.get()