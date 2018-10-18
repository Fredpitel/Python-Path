import csv
import Tkinter as  tk

from Modifiable       import *
from Model.skillTree  import SkillTree
from math             import floor

class Character():
    BASE_ABILITY_VALUE = 10
    BASE_AC_VALUE      = 10
    MAX_LEVEL          = 20

    def __init__(self, controller):
        self.controller   = controller

        self.charName     = tk.StringVar()
        self.charLevel    = tk.IntVar(value=0)
        self.levels       = []
        self.charClass    = {}

        self.race         = tk.StringVar(value="Choose race")
        self.alignment    = tk.StringVar(value="Choose alignment")
        self.deity        = tk.StringVar(value="None")
        self.hpFromLevels = tk.IntVar(value=0)
        self.spFromLevels = tk.IntVar(value=0)

        # Modifiables
        self.str = AbilityScore(self.BASE_ABILITY_VALUE,"STRENGTH","str") 
        self.con = AbilityScore(self.BASE_ABILITY_VALUE,"CONSTITUTION","con") 
        self.dex = AbilityScore(self.BASE_ABILITY_VALUE,"DEXTERITY","dex") 
        self.int = AbilityScore(self.BASE_ABILITY_VALUE,"INTELLIGENCE","int") 
        self.wis = AbilityScore(self.BASE_ABILITY_VALUE,"WISDOM","wis") 
        self.cha = AbilityScore(self.BASE_ABILITY_VALUE,"CHARISMA","cha") 

        self.ac           = AC(self.BASE_AC_VALUE)
        self.attack       = Attack(0, self)
        self.cmb          = CMB(0)
        self.cmd          = CMD(0)
        self.fortitude    = Fortitude(0, self)
        self.reflex       = Reflex(0, self)
        self.will         = Will(0, self)
        self.skillPoints  = SkillPoints(0, self)
        self.spentSP      = 0
        self.hp           = HP(0, self)

        self.babString    = tk.StringVar()


    def createSkillTree(self, controller):
        self.skill        = SkillTree(self.controller)


    def getBab(self):
        bab = 0
        for className in self.charClass:
            charClass = self.charClass[className]

            bab += charClass.attackProg * charClass.nbLevels

        return int(floor(bab))