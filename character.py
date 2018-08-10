import ttk
import csv

from tkinter     import *
from math        import *
from decimal     import *

from nestledDict import NestledDict
from skillTree   import SkillTree

class Character:
    BASE_ABILITY_VALUE = 10
    BASE_AC_VALUE      = 10
    MAX_LEVEL          = 20
    ABILITY_SHORT      = ["str","dex","con","int","wis","cha"]
    STACKABLE_TYPES    = ["dodge", "untyped"]

    def __init__(self):
        self.charName = StringVar()

        # Total Ability Score
        self.str = IntVar(value=self.BASE_ABILITY_VALUE)
        self.dex = IntVar(value=self.BASE_ABILITY_VALUE)
        self.con = IntVar(value=self.BASE_ABILITY_VALUE)
        self.int = IntVar(value=self.BASE_ABILITY_VALUE)
        self.wis = IntVar(value=self.BASE_ABILITY_VALUE)
        self.cha = IntVar(value=self.BASE_ABILITY_VALUE)

        # Base Ability Score (includes point buy and score increases)
        self.strBase = IntVar(value=self.BASE_ABILITY_VALUE)
        self.dexBase = IntVar(value=self.BASE_ABILITY_VALUE)
        self.conBase = IntVar(value=self.BASE_ABILITY_VALUE)
        self.intBase = IntVar(value=self.BASE_ABILITY_VALUE)
        self.wisBase = IntVar(value=self.BASE_ABILITY_VALUE)
        self.chaBase = IntVar(value=self.BASE_ABILITY_VALUE)

        # Ability Score Bonus
        self.strBonus = IntVar(value=0)
        self.dexBonus = IntVar(value=0)
        self.conBonus = IntVar(value=0)
        self.intBonus = IntVar(value=0)
        self.wisBonus = IntVar(value=0)
        self.chaBonus = IntVar(value=0)

        self.modifiers = NestledDict()
        
        self.race         = StringVar(value="Choose race")
        self.skill        = SkillTree()
        self.ac           = IntVar(value=self.BASE_AC_VALUE)
        self.attack       = IntVar(value=0)
        self.cmb          = IntVar(value=0)
        self.cmd          = IntVar(value=0)
        self.savingThrows = IntVar(value=0)

        self.charLevel = IntVar(value=0)
        self.levels = []

    def updateAbilityScore(self, stat):
        eval("self." + stat).set((eval("self." + stat + "Base").get()) + self.getModValue(stat))
        eval("self." + stat + "Bonus").set(floor((eval("self." + stat).get() - self.BASE_ABILITY_VALUE)/2))

    def updateMods(self, target):
        total = self.getModValue(target)

        targetVar = eval("self." + target)
        targetVar.set(targetVar.get() + total)

        if target in self.ABILITY_SHORT:
            self.updateAbilityScore(target)


    def getModValue(self, target):
        total = 0
        for type in self.modifiers[target].keys():
            if type in self.STACKABLE_TYPES:
                for source in type.keys():
                    total += type[source]
            else:
                maxMod = {"source": "", "value": Decimal('-Infinity')}
                for source in self.modifiers[target][type].keys():
                    if self.modifiers[target][type][source] > maxMod["value"] and source != maxMod["source"]:
                        maxMod = {"source": source, "value": self.modifiers[target][type][source]}

                total += maxMod["value"]

        return total


    def removeMods(self, source):
        for target in self.modifiers.keys():
            for type in self.modifiers[target].keys():
                for modSource in self.modifiers[target][type].keys():
                    if modSource == source:
                        targetVar = eval("self." + target)
                        targetVar.set(targetVar.get() - self.modifiers[target][type][modSource])
                        del self.modifiers[target][type][modSource]

                        if not self.modifiers[target][type]:
                            del self.modifiers[target][type]
                            if not self.modifiers[target]:
                                del self.modifiers[target]

                        if target in self.ABILITY_SHORT:
                            self.updateAbilityScore(target)