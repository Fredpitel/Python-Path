import ttk
import csv

from tkinter     import *

from nestledDict import *
from Modifiable  import *
from level       import *
from error       import *

class Character:
    BASE_ABILITY_VALUE = 10
    BASE_AC_VALUE      = 10
    MAX_LEVEL          = 20
    ABILITY_SHORT      = ["str","dex","con","int","wis","cha"]
    STACKABLE_TYPES    = ["dodge", "untyped"]

    def __init__(self):
        self.charName  = StringVar()
        self.modifiers = NestledDict()
        self.charLevel = IntVar(value=0)
        self.levels    = []
        self.charClass = {} 
        self.race      = StringVar(value="Choose race")
        self.favClass  = StringVar(value="Choose favorite class")

        # Modifiables
        self.str = AbilityScore(self,self.BASE_ABILITY_VALUE,"STRENGTH","str") 
        self.con = AbilityScore(self,self.BASE_ABILITY_VALUE,"CONSTITUTION","con") 
        self.dex = AbilityScore(self,self.BASE_ABILITY_VALUE,"DEXTERITY","dex") 
        self.int = AbilityScore(self,self.BASE_ABILITY_VALUE,"INTELLIGENCE","int") 
        self.wis = AbilityScore(self,self.BASE_ABILITY_VALUE,"WISDOM","wis") 
        self.cha = AbilityScore(self,self.BASE_ABILITY_VALUE,"CHARISMA","cha") 

        self.skill        = SkillTree(self)
        self.ac           = AC(self,self.BASE_AC_VALUE)
        self.attack       = Attack(self,0)
        self.cmb          = CMB(self,0)
        self.cmd          = CMD(self,0)
        self.savingThrows = SavingThrows(self,0)
        self.skillPoints  = SkillPoints(self,0)
        self.hp           = HP(self,0)
        
        self.errors = []


    def removeMods(self, source):
        targetsToUpdate = []

        for target in self.modifiers.keys():
            for type in self.modifiers[target].keys():
                for modSource in self.modifiers[target][type].keys():
                    if modSource == source:
                        del self.modifiers[target][type][modSource]

                        if not self.modifiers[target][type]:
                            del self.modifiers[target][type]
                            if not self.modifiers[target]:
                                del self.modifiers[target]

                        targetsToUpdate.append(target)

        for target in targetsToUpdate:
            target.update()


    def addLevel(self, charClass, hp, hitDie, favClassVar, favClassBonusMenu):
        level = Level(self, charClass, hp, hitDie, favClassVar, favClassBonusMenu, charClass == self.favClass.get())
        self.levels.append(level)
        
        if not level.active.get():
            level.favClassBonusMenu.configure(state="disabled")

        self.checkFavClassBonuses()

        try:
            self.charClass[charClass] += 1
        except:
            self.charClass[charClass] = 1


    def removeLevel(self, index):
        level = self.levels.pop(index)
        if len(self.levels) > 0:
            self.levels[0].hpGained.set(self.levels[0].hitDie)

        self.charClass[level.charClass] -= 1
        if self.charClass[level.charClass] == 0:
            error = self.findErrorBySource(level.charClass)
            if error != None:
                self.removeError(error)

            del self.charClass[level.charClass]
        
        self.checkFavClassBonuses()
        self.removeMods(level)
        self.charLevel.set(self.charLevel.get() - 1)


    def addError(self, source, message, problem):
        problem.config(fg="red")
        
        for error in self.errors:
            if error.source == source:
                return

        error = Error(source, message, self.errorFrame, problem)
        self.errors.append(error)

        return error


    def removeError(self, error):
        if error in self.errors:
            try:
                error.problem.config(fg="black")
            except:
                pass
            error.label.destroy()
            self.errors.remove(error)


    def findErrorBySource(self, source):
        for error in self.errors:
            if error.source == source:
                return error


    def checkFavClassBonuses(self):
        stillError = False

        try:
            self.removeError(self.favClassBonusError)
        except:
            pass

        for level in self.levels:
            if level.favClassVar.get() == "Choose Bonus" and level.active.get():
                level.favClassBonusMenu.config(fg="red")
                stillError = True
            elif level.active.get():
                level.favClassBonusMenu.config(fg="black")

        if stillError:
            self.favClassBonusError = self.addError(level.favClassVar.get(), "Choose favorite class bonus", level.favClassBonusMenu)
            return

        error = self.findErrorBySource("Choose Bonus")
        if error != None:
            self.removeError(error)