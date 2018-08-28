from tkinter  import *

class Level:
    def __init__(self, char, charClass, hpVar, hitDie, favClassVar, favClassBonusMenu, active):
        self.char        = char
        self.charClass   = charClass
        self.hitDie      = hitDie
        
        self.hpVar       = hpVar
        self.hpVar.trace("w", self.validateEntry)
        
        self.hpGained    = IntVar(value=hpVar.get())
        self.hpGained.trace("w", lambda i,o,x: self.char.hp.update())
        
        self.favClassVar = favClassVar
        self.favClassVar.trace("w", self.updateFavClassBonus)

        self.favClassBonusMenu = favClassBonusMenu

        self.active = BooleanVar(value=active)
        self.active.trace("w", self.updateFavClassBonus)


    def validateEntry(self,i,o,x):
        value = self.hpVar.get()

        if value == "":
            self.hpGained.set(0)
            return
        else:
            try:
                value = int(value)
                if value  < 1:
                    value = 1
                elif value > self.hitDie:
                    value = self.hitDie
            except ValueError:
                value = self.hpGained.get()

        self.hpVar.set(str(value))
        self.hpGained.set(value)


    def updateFavClassBonus(self,i,o,x):
        self.char.removeMods(self)

        if not self.active.get():
            return

        if self.favClassVar.get() == "Choose Bonus":
            self.char.addError(self.favClassVar.get(), "Choose favorite class bonus", self.favClassBonusMenu)
            return

        self.char.checkFavClassBonuses()
        
        if self.favClassVar.get() == "+1 Hit Point":
            target = self.char.hp
        elif self.favClassVar.get() == "+1 Skill Point":
            target = self.char.skillPoints

        self.char.modifiers[target]["untyped"][self] = 1
        target.update()
