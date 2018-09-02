import csv
import Tkinter as  tk


from Modifiable       import *
from Model.error      import Error
from Model.skillTree  import SkillTree
from Util.nestledDict import NestledDict

class Character():
    BASE_ABILITY_VALUE = 10
    BASE_AC_VALUE      = 10
    MAX_LEVEL          = 20
    ABILITY_SHORT      = ["str","dex","con","int","wis","cha"]
    STACKABLE_TYPES    = ["dodge", "untyped"]

    def __init__(self, controller):
        self.charName     = tk.StringVar()
        self.modifiers    = NestledDict()
        self.charLevel    = tk.IntVar(value=0)
        self.levels       = []
        self.charClass    = {}
        self.race         = tk.StringVar(value="Choose race")
        self.alignment    = tk.StringVar(value="Choose alignment")
        self.hpFromLevels = tk.IntVar(value=0)

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


    def addMod(self, targetName, type, source, value):
        target = self.getTarget(targetName)
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


    def getTarget(self, targetName):
        try:
            return getattr(self, targetName)
        except AttributeError:
            skill = targetName.split('"')[1]
            return self.skill[skill]