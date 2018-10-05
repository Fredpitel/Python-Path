#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import json
import os

from View.creationPage     import CreationPage
from View.levelFrame       import LevelFrame
from View.advancementFrame import AdvancementFrame
from View.languageWindow   import LanguageWindow
from Model.error           import Error

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

    ADVANCEMENT     = [
                        "+1 Strength",
                        "+1 Dexterity",
                        "+1 Constitution",
                        "+1 Intelligence",
                        "+1 Wisdom",
                        "+1 Charisma"
                    ]

    HUMANLIKE_RACES = ["Human", "Half-Elf", "Half-Orc"]
    ALIGNMENTS      = ["LG","NG","CG","LN","TN","CN","LE","NE","CE"]


    def __init__(self, controller):
        self.controller              = controller
        self.char                    = controller.char
 
        self.levelFrames             = []
        self.advancementFrames       = []
        self.languageFrames          = []
        self.errors                  = []
        self.races                   = []
        self.classes                 = []
        self.deities                 = ["None"]
        self.classRequirements       = {}
        self.advancementRequirement  = None
        self.abilityBonusRequirement = None
        self.languageRequirement     = None

        # Global character variables
        self.charName  = self.char.charName
        self.race      = self.char.race
        self.alignment = self.char.alignment
        self.deity     = self.char.deity

        # CreationPage specific variables
        self.buyPoints      = tk.IntVar(value=0)
        self.maxBuyPoints   = tk.IntVar(value=15)
        self.purchaseMode   = tk.StringVar(value="Standard Fantasy (15 points)")
        self.bonusAbility   = tk.StringVar(value="Choose ability bonus")
        self.strBonusStr    = tk.StringVar(value="STR (+0)")
        self.dexBonusStr    = tk.StringVar(value="DEX (+0)")
        self.conBonusStr    = tk.StringVar(value="CON (+0)")
        self.intBonusStr    = tk.StringVar(value="INT (+0)")
        self.wisBonusStr    = tk.StringVar(value="WIS (+0)")
        self.chaBonusStr    = tk.StringVar(value="CHA (+0)")
        self.charClass      = tk.StringVar(value="Choose class")
        self.favClass       = tk.StringVar(value="Choose favorite class")
        self.levelNb        = tk.IntVar(value=1)
        self.advancement    = tk.StringVar(value="Choose Bonus")
        self.bonusLanguages = tk.IntVar(value=0)
        self.addedLanguages = tk.IntVar(value=0)

        # Data
        self.race_data = json.load(open(os.path.abspath("Data/races.json")))
        for race in self.race_data:
            self.races.append(race)

        self.races.sort()

        self.class_data = json.load(open(os.path.abspath("Data/classes.json")))
        for className in self.class_data:
            self.classes.append(className)

        self.classes.sort()

        self.deity_data = json.load(open(os.path.abspath("Data/deities.json")))
        for deity in self.deity_data:
            self.deities.append(deity)


        # Tracing
        self.char.str.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.str))
        self.char.dex.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.dex))
        self.char.con.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.con))
        self.char.int.bonus.trace("w", lambda i,o,x: self.setAbilityBonusString(self.char.int))
        self.char.int.bonus.trace("w", lambda i,o,x: self.checkBonusLanguages(self.char.int.bonus.get()))
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
                if self.abilityBonusRequirement is None:
                    self.abilityBonusRequirement = self.controller.addRequirement(
                                                                        [self.bonusAbility],
                                                                        lambda: (self.bonusAbility.get() != "Choose ability bonus", None),
                                                                        "Choose racial ability bonus",
                                                                        [self.view.abilityMenu]
                                                                    )
            else:
                self.setBonusAbility()
        else:
            self.view.abilityMenu.grid_remove()        

        for frame in self.levelFrames:
            frame.favClassBonusMenu['menu'].delete(0, 'end')
            
            options = ["+1 Hit Point", "+1 Skill Point"]
            special = data["favoredClassOptions"][frame.charClass.get()]["menuString"]
            options.append(special)

            for option in options:
                frame.favClassBonusMenu["menu"].add_command(label=option,command=tk._setit(frame.favClassBonus, option))

        for frame in list(self.languageFrames):
            self.removeLanguage(frame)

        for language in data["languages"]:
            self.languageFrames.append(self.view.addLanguageFrame(language, True))


    def removeLanguage(self, frame):
        self.languageFrames.remove(frame)
        frame.pack_forget()

        if not frame.racial:
            self.addedLanguages.set(self.addedLanguages.get() - 1)


    def checkBonusLanguages(self, intBonus):
        self.bonusLanguages.set(intBonus)

        if self.bonusLanguages.get() != self.addedLanguages.get() and self.languageRequirement is None:
            self.languageRequirement = self.controller.addRequirement([self.bonusLanguages, self.addedLanguages],
                                                                     lambda: self.checkAddedLanguages(),
                                                                     "",
                                                                     [self.view.addLanguageButton])


    def checkAddedLanguages(self):
        if self.bonusLanguages.get() < self.addedLanguages.get() and self.bonusLanguages.get() > 0:
            self.view.addLanguageButton.config(fg="red")
            return (False, "Too many bonus languages chosen")
        elif self.bonusLanguages.get() > self.addedLanguages.get():
            self.view.addLanguageButton.config(state="normal", fg="red")
            return (False, "Bonus language remain to be chosen")
        else:
            self.view.addLanguageButton.config(state="disabled")
            return (True, None)


    def createLanguageWindow(self):
        languages = []

        if self.char.race.get() != "Choose race":
            for language in self.race_data[self.char.race.get()]["bonusLanguages"]:
                ok = True
                for frame in self.languageFrames:
                    if frame.language == language:
                        ok = False
                        break
                if ok:
                    languages.append(language)

        remaining = self.bonusLanguages.get() - self.addedLanguages.get()

        LanguageWindow(self, languages, remaining)


    def addBonusLanguages(self, window, checkboxes):
        window.destroy()

        for checkbox in checkboxes:
            if checkbox.var.get():
                self.languageFrames.append(self.view.addLanguageFrame(checkbox.language, False))
                self.addedLanguages.set(self.addedLanguages.get() + 1)


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

        for i in range(len(self.advancementFrames), self.char.charLevel.get() / 4):
            frame = AdvancementFrame(self.view.advancementFrame, self, i+1, True)
            self.advancementFrames.append(frame)
            self.addAdvancementRequirement(frame)

        if len(self.advancementFrames) < self.char.charLevel.get() / 4 + 1:
            self.advancementFrames.append(AdvancementFrame(self.view.advancementFrame, self, len(self.advancementFrames)+1, False))

        lvlsToAdd.set(1)


    def addAdvancementRequirement(self, frame):
        if self.advancementRequirement is None:
            self.advancementRequirement = self.controller.addRequirement([frame.bonus, frame.isActive],
                                                                         lambda: self.checkAdvancementRequirement(),
                                                                         "Ability bonus remain to be chosen",
                                                                         [frame.menu])
        else:
            self.advancementRequirement.addTarget(frame.bonus)
            self.advancementRequirement.addTarget(frame.isActive)
            self.advancementRequirement.addProblem(frame.menu)


    def addCharClassRequirements(self, charClass):
        self.classRequirements[charClass] = []

        for req in self.class_data[charClass]["requirements"]:
            target = [self.controller.getTarget(req["type"])]
            values = req["value"]

            if charClass == "Cleric":
                target.append(self.char.deity)
                condition = lambda: (self.checkClericAlignments(), None)
            else:
                condition = lambda c=charClass, v=values: (self.checkAlignment(c,v), None)

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
            self.view.buyPointsLabel.config(fg="red")
            return (False, "Too many buy points spent")
        elif self.maxBuyPoints.get() > self.buyPoints.get():
            self.view.buyPointsLabel.config(fg="red")
            return (False, "Buy points remain to be spent")
        else:
            return (True, None)


    def checkFavClassBonusError(self):
        res = (True, None)

        for frame in self.levelFrames:
            if frame.favClassBonus.get() == "Choose Bonus" and frame.isFavClass.get():
                frame.favClassBonusMenu.config(fg="red")
                res = (False, None)
            else:
                frame.favClassBonusMenu.config(fg="black")

        return res


    def checkAdvancementRequirement(self):
        res = (True, None)

        for frame in self.advancementFrames:
            if frame.isActive.get() and frame.bonus.get() == "Choose Bonus":
                frame.menu.config(fg="red")
                res = (False, None)
            else:
                frame.menu.config(fg="black")


        return res


    def calculateHpGainedFromLevels(self):
        total = 0
        for frame in self.levelFrames:
            total += frame.hpGained.get()

        self.char.hpFromLevels.set(total)


    def checkAlignment(self, charClass, values):
        if self.char.alignment.get() in values:
            return True
        else:
            for req in self.classRequirements[charClass]:
                for problem in req.problems:
                    problem.config(fg="red")

            return False


    def checkClericAlignments(self):
        res = False

        chosenDeity = self.char.deity.get()
        deityAlignments = []

        if chosenDeity != "None":
            deityAlignments = self.deity_data[chosenDeity]["alignments"]

        if self.char.alignment.get() in deityAlignments:
            res = True
        else:
            for req in self.classRequirements["Cleric"]:
                for problem in req.problems:
                    problem.config(fg="red")

        return res