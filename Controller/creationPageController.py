#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as  tk
import json
import os

from View.creationPage import CreationPage
from View.levelFrame   import LevelFrame
from Model.error       import Error

class CreationPageController():
    POINT_BUY_CHART = {
        7: -4,
        8: -2,
        9: -1,
        10: 0,
        11: 1,
        12: 2,
        13: 3,
        14: 5,
        15: 7,
        16: 10,
        17: 13,
        18: 17
    }

    PURCHASE_MODES = [
                        "Low Fantasy (10 points)",
                        "Standard Fantasy (15 points)",
                        "High Fantasy (20 points)",
                        "Epic Fantasy (25 points)"
                    ]

    ABILITY_BONUS   = [
                        "+2 Strength",
                        "+2 Dexterity",
                        "+2 Constitution",
                        "+2 Intelligence",
                        "+2 Wisdom",
                        "+2 Charisma"
                    ]

    HUMANLIKE_RACES = ["Human", "Half-Elf", "Half-Orc"]
    ALIGNMENTS      = ["","LG","NG","CG","LN","TN","CN","LE","NE","CE"]
    RACES = []
    CLASSES = []

    def __init__(self, controller):
        self.controller   = controller
        self.char         = controller.char
        self.levelFrames  = []
        self.errors       = []

        # Global character variables
        self.charName     = self.char.charName
        self.race         = self.char.race
        self.alignment    = self.char.alignment

        # CreationPage specific variables
        self.buyPoints    = tk.IntVar(value=0)
        self.maxBuyPoints = tk.IntVar(value=15)
        self.purchaseMode = tk.StringVar(value="Standard Fantasy (15 points)")
        self.bonusAbility = tk.StringVar(value="Choose ability bonus")
        self.strBonusStr  = tk.StringVar(value="STR (+0)")
        self.dexBonusStr  = tk.StringVar(value="DEX (+0)")
        self.conBonusStr  = tk.StringVar(value="CON (+0)")
        self.intBonusStr  = tk.StringVar(value="INT (+0)")
        self.wisBonusStr  = tk.StringVar(value="WIS (+0)")
        self.chaBonusStr  = tk.StringVar(value="CHA (+0)")
        self.charClass    = tk.StringVar(value="Choose class")
        self.favClass     = tk.StringVar(value="Choose favorite class")
        self.levelNb      = tk.IntVar(value=1)

        # Data
        self.race_data = json.load(open(os.path.abspath("Data/races.json")))
        for race in self.race_data:
            self.RACES.append(race)

        self.RACES.sort()

        self.class_data = json.load(open(os.path.abspath("Data/classes.json")))
        for className in self.class_data:
            self.CLASSES.append(className)

        self.CLASSES.sort()

        # Tracing
        self.char.str.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.str))
        self.char.dex.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.dex))
        self.char.con.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.con))
        self.char.int.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.int))
        self.char.wis.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.wis))
        self.char.cha.bonus.trace("w", lambda i,x,o: self.setAbilityBonusString(self.char.cha))
        self.purchaseMode.trace(  "w", lambda i,x,o: self.setPurchaseMode(self.purchaseMode.get()))
        self.charName.trace(      "w", lambda i,x,o: self.char.charName.set(self.charName.get()))
        self.bonusAbility.trace(  "w", lambda i,o,x: self.setBonusAbility())
        self.char.charLevel.trace("w", lambda i,o,x: self.setRemainingLevels)
        self.charClass.trace(     "w", lambda i,o,x: self.view.addLevelsButton.config(state="normal"))
        self.char.race.trace(     "w", self.setRace)
        self.alignment.trace(     "w", self.setAlignment)
        self.favClass.trace(      "w", lambda i,o,x: self.setFavClass())

        # View
        self.view = CreationPage(self, controller.nb)


    def getView(self):
        return self.view.creationPage


    def getModifiableValue(self, modifiable):
        return getattr(self.char, modifiable).value


    def setAbilityBonusString(self, stat):
        sign = "+" if stat.bonus.get() >= 0 else ""
        getattr(self, stat.shortName + "BonusStr").set(stat.shortName.upper() + " (" + sign + "%d)" % stat.bonus.get())


    def setPurchaseMode(self, purchaseMode):
        if purchaseMode == "Low Fantasy (10 points)":
            self.maxBuyPoints.set(10)
        elif purchaseMode == "Standard Fantasy (15 points)":
            self.maxBuyPoints.set(15)
        elif purchaseMode == "High Fantasy (20 points)":
            self.maxBuyPoints.set(20)
        else:
            self.maxBuyPoints.set(25)


    def setAbilityScore(self, stat, value):
        charStat = getattr(self.char, stat)
        current = charStat.baseValue.get()
        new = current + value

        if new >= 7 and new <= 18:
            charStat.baseValue.set(new)

            previousPoints = self.POINT_BUY_CHART[current]
            self.buyPoints.set(self.buyPoints.get() - previousPoints)

            points = self.POINT_BUY_CHART[new]
            self.buyPoints.set(self.buyPoints.get() + points)


    def setAbilityAdvancement(self,i,o,x):
        pass


    def setRemainingLevels(self):
        if self.char.charLevel.get() == self.char.MAX_LEVEL:
            self.view.addLevelsButton.config(state="disabled")
        else:
            self.view.addLevelsButton.config(state="normal")


    def setRace(self,i,o,x):
        race = self.char.race
        data = self.race_data[race.get()]

        for mod in data["mods"]:
            self.controller.addMod(mod, race, self.view.racesMenu)

        if race.get() in self.HUMANLIKE_RACES:
            self.view.abilityMenu.grid()
            if self.bonusAbility.get() == "Choose ability bonus":
                self.controller.addError("Choose racial ability bonus", [self.bonusAbility], self.view.abilityMenu)
        else:
            self.view.abilityMenu.grid_remove()        

        for frame in self.levelFrames:
            frame.favClassBonusMenu['menu'].delete(0, 'end')
            
            options = ["+1 Hit Point", "+1 Skill Point"]
            special = data["favoredClassOptions"][frame.charClass.get()]["menuString"]
            options.append(special)

            for option in options:
                frame.favClassBonusMenu["menu"].add_command(label=option,command=tk._setit(frame.favClassBonus, option))


    def setBonusAbility(self):
        bonus = self.bonusAbility.get()

        if bonus == "+2 Strength":
            stat = "str"
        elif bonus == "+2 Dexterity":
            stat = "dex"
        elif bonus == "+2 Constitution":
            stat = "con"
        elif bonus == "+2 Intelligence":
            stat = "int"
        elif bonus == "+2 Wisdom":
            stat = "wis"
        else:
            stat = "cha"
        
        self.controller.addMod({"target": stat, "type": "racial", "value": 2}, self.bonusAbility, self.view.abilityMenu)
            
    

    def setLevelNb(self, value):
        current   = self.levelNb.get()
        new       = current + value
        remaining = self.char.MAX_LEVEL - self.char.charLevel.get()

        if new >= 1 and new <= remaining:
            self.levelNb.set(new)


    def setAlignment(self,i,o,x):
        for frame in self.levelFrames:
            className = charClass.winfo_children()[1]
            className.config(fg="black")

            alignmentArray = self.class_data["classes"][className.cget("text")]["alignment"]

            error = self.char.findErrorBySource(className.cget("text"))


            if len(alignmentArray) > 0 and self.alignment.get() not in alignmentArray:
                className.config(fg="red")
                message = self.class_data["classes"][className.cget("text")]["alignmentMsg"]
                self.char.addError(message, self.char.alignment, self.view.alignmentMenu)


    def setFavClass(self):
        for frame in self.levelFrames:
            if frame.charClass.get() == self.favClass.get():
                frame.isFavClass.set(True)
                frame.favClassBonusMenu.config(state="normal")
                if frame.isFavClass.get() and frame.favClassBonus.get() == "Choose Bonus":
                    self.controller.addError("",
                                             [frame.isFavClass, frame.favClassBonus],
                                             frame.favClassBonusMenu)
            else:
                frame.isFavClass.set(False)
                frame.favClassBonusMenu.config(state="disabled")

        self.checkFavClassBonusError()


    def addLevels(self):
        currentLvl = self.char.charLevel.get()
        lvlsToAdd  = self.levelNb
        charClass  = self.charClass.get()
        hitDie     = self.class_data[charClass]["hitDie"]
        race       = self.race.get()
        isFavClass = True if self.favClass.get() == charClass else False

        if currentLvl == 0:
            self.view.favClassMenu.grid()
            if self.favClass.get() == "Choose favorite class":
                self.controller.addError("Choose a favorite class", [self.favClass], self.view.favClassMenu)

        for i in range(currentLvl, currentLvl + lvlsToAdd.get()):
            frame = LevelFrame(self.view.charClassFrame, self, i, charClass, hitDie, isFavClass)

            if race != "Choose race":
                special = self.race_data[race]["favoredClassOptions"][charClass]["menuString"]
                frame.favClassBonusMenu["menu"].add_command(label=special,command=tk._setit(frame.favClassBonus, special))

            self.levelFrames.append(frame)
            self.char.hp.baseValue.set(self.char.hp.baseValue.get() + frame.hpGained.get())
            if frame.isFavClass.get():
                self.controller.addError("Choose favorite class bonus",
                                         [self.favClass],
                                         None)
                self.controller.addError("",
                                         [frame.isFavClass, frame.favClassBonus],
                                         frame.favClassBonusMenu)

        self.char.charLevel.set(currentLvl + lvlsToAdd.get())
        lvlsToAdd.set(1)


    def removeLevel(self, levelFrame):
        for i in range(levelFrame.levelNumber.get(), len(self.levelFrames)):
            self.levelFrames[i].levelNumber.set(self.levelFrames[i].levelNumber.get() - 1)

        self.levelFrames.remove(levelFrame)
        self.char.charLevel.set(self.char.charLevel.get() - 1)
        levelFrame.frame.destroy()

        if self.char.charLevel.get() == 0:
            self.view.favClassMenu.grid_remove()

        self.checkFavClassBonusError()


    def checkBuyPointsError(self):
        if self.maxBuyPoints.get() < self.buyPoints.get():
            return (False, "Too many buy points spent")
        elif self.maxBuyPoints.get() > self.buyPoints.get():
            return (False, "Buy points remain to be spent")
        else:
            return (True, None)


    def checkFavClassBonusError(self):
        self.controller.removeError(self.controller.findErrorBySolution(self.favClass))
        for frame in self.levelFrames:
            if frame.favClassBonus.get() == "Choose Bonus" and frame.isFavClass.get():
                self.controller.addError("Choose favorite class bonus",
                                         [self.favClass],
                                         None)
                return