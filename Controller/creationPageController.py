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
    ALIGNMENTS      = ["LG","NG","CG","LN","TN","CN","LE","NE","CE"]
    DEITIES         = ["None"]
    RACES           = []
    CLASSES         = []

    def __init__(self, controller):
        self.controller        = controller
        self.char              = controller.char
        self.levelFrames       = []
        self.errors            = []
        self.classRequirements = {}

        # Global character variables
        self.charName     = self.char.charName
        self.race         = self.char.race
        self.alignment    = self.char.alignment
        self.deity        = self.char.deity

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

        self.deity_data = json.load(open(os.path.abspath("Data/deities.json")))
        for deity in self.deity_data:
            self.DEITIES.append(deity)


        # Tracing
        self.char.str.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.str))
        self.char.dex.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.dex))
        self.char.con.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.con))
        self.char.int.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.int))
        self.char.wis.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.wis))
        self.char.cha.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.cha))
        self.char.charLevel.trace("w", lambda i,o,x: self.calculateHpGainedFromLevels())
        self.purchaseMode.trace(  "w", lambda i,o,x: self.setPurchaseMode(self.purchaseMode.get()))
        self.charName.trace(      "w", lambda i,o,x: self.char.charName.set(self.charName.get()))
        self.bonusAbility.trace(  "w", lambda i,o,x: self.setBonusAbility())
        self.char.charLevel.trace("w", lambda i,o,x: self.setRemainingLevels)
        self.charClass.trace(     "w", lambda i,o,x: self.view.addLevelsButton.config(state="normal"))
        self.char.race.trace(     "w", lambda i,o,x: self.setRace())
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


    def setAbilityAdvancement(self):
        pass


    def setRemainingLevels(self):
        if self.char.charLevel.get() == self.char.MAX_LEVEL:
            self.view.addLevelsButton.config(state="disabled")
        else:
            self.view.addLevelsButton.config(state="normal")


    def setRace(self):
        race = self.char.race
        data = self.race_data[race.get()]

        for mod in data["mods"]:
            self.controller.addMod(mod, race, self.view.racesMenu)

        if race.get() in self.HUMANLIKE_RACES:
            self.view.abilityMenu.grid()
            if self.bonusAbility.get() == "Choose ability bonus":
                self.controller.addRequirement(
                        [self.bonusAbility],
                        lambda: (self.bonusAbility.get() != "Choose ability bonus", None),
                        "Choose racial ability bonus",
                        [self.view.abilityMenu]
                    )
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


    def setFavClass(self):
        for frame in self.levelFrames:
            if frame.charClass.get() == self.favClass.get():
                frame.isFavClass.set(True)
            else:
                frame.isFavClass.set(False)


    def addLevels(self):
        currentLvl = self.char.charLevel.get()
        lvlsToAdd  = self.levelNb
        charClass  = self.charClass.get()

        if charClass not in self.classRequirements:
            self.addCharClassRequirements(charClass)

        for i in range(currentLvl, currentLvl + lvlsToAdd.get()):
            self.addLevelFrame(charClass, i)


        self.char.charLevel.set(currentLvl + lvlsToAdd.get())
        lvlsToAdd.set(1)


    def addCharClassRequirements(self, charClass):
        self.classRequirements[charClass] = []

        for req in self.class_data[charClass]["requirements"]:
            target = [self.controller.getTarget(req["type"])]
            values = req["value"]

            if charClass == "Cleric":
                target.append(self.char.deity)
                condition = lambda: (self.checkClericAlignments(), None)
            else:
                condition = lambda t=target, v=values: (t[0].get() in v, None)

            self.classRequirements[charClass].append(
                self.controller.addRequirement(
                    target,
                    condition,
                    req["message"],
                    []
                )
            )


    def addLevelFrame(self, charClass, index):
        hitDie     = self.class_data[charClass]["hitDie"]
        race       = self.race.get()
        isFavClass = True if self.favClass.get() == charClass else False

        frame = LevelFrame(self.view.charClassFrame, self, index, charClass, hitDie, isFavClass)

        if race != "Choose race":
            special = self.race_data[race]["favoredClassOptions"][charClass]["menuString"]
            frame.favClassBonusMenu["menu"].add_command(label=special,command=tk._setit(frame.favClassBonus, special))

        self.levelFrames.append(frame)

        frame.hpGained.trace("w", lambda i,o,x: self.calculateHpGainedFromLevels())

        self.updateFavClassBonusRequirement(frame, index)

        for req in self.classRequirements[charClass]:
            req.addProblem(frame.classLabel)


    def updateFavClassBonusRequirement(self, frame, index):
        if index == 0:
            self.view.favClassMenu.grid()
            self.controller.addRequirement(
                [self.favClass],
                lambda: (self.favClass.get() != "Choose favorite class", None),
                "Choose a favorite class",
                [self.view.favClassMenu]
            )
            self.favClassBonusRequirement = self.controller.addRequirement(
                                                [frame.favClassBonus, frame.isFavClass],
                                                lambda: self.checkFavClassBonusError(),
                                                "Favorite class bonus remain to be chosen",
                                                [frame.favClassBonusMenu]
                                            )
        else:
            self.favClassBonusRequirement.addTarget(frame.favClassBonus)
            self.favClassBonusRequirement.addTarget(frame.isFavClass)
            self.favClassBonusRequirement.addProblem(frame.favClassBonusMenu)


    def removeLevel(self, levelFrame):
        for i in range(levelFrame.levelNumber.get(), len(self.levelFrames)):
            self.levelFrames[i].levelNumber.set(self.levelFrames[i].levelNumber.get() - 1)

        self.levelFrames.remove(levelFrame)
        self.char.charLevel.set(self.char.charLevel.get() - 1)
        levelFrame.frame.pack_forget()

        if self.char.charLevel.get() == 0:
            self.view.favClassMenu.grid_remove()


    def checkBuyPointsError(self):
        if self.maxBuyPoints.get() < self.buyPoints.get():
            return (False, "Too many buy points spent")
        elif self.maxBuyPoints.get() > self.buyPoints.get():
            return (False, "Buy points remain to be spent")
        else:
            return (True, None)


    def checkFavClassBonusError(self):
        res = (True, None)

        for frame in self.levelFrames:
            if frame.favClassBonus.get() == "Choose Bonus" and frame.isFavClass.get():
                res = (False, None)
        
        return res


    def calculateHpGainedFromLevels(self):
        total = 0
        for frame in self.levelFrames:
            total += frame.hpGained.get()

        self.char.hpFromLevels.set(total)


    def checkClericAlignments(self):
        res = False

        chosenDeity = self.char.deity.get()

        if chosenDeity != "None":
            deityAlignments = self.deity_data[chosenDeity]["alignments"]

            if self.char.alignment.get() in deityAlignments:
                res = True

        return res