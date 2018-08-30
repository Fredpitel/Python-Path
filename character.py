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
        self.charName     = StringVar()
        self.modifiers    = NestledDict()
        self.charLevel    = IntVar(value=0)
        self.levels       = []
        self.charClass    = {}
        self.race         = StringVar(value="Choose race")
        self.alignment    = StringVar(value="Choose alignment")#
        self.hpFromLevels = IntVar(value=0)

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


    def addMod(self, target, type, source, value):
        self.modifiers[target][type][source] = value
        target.update()


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