#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from tkinter  import *

class classPageController:
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

    RACES = []
    CLASSES = []

    HUMANLIKE_RACES = ["Human", "Half-Elf", "Half-Orc"]
    ABILITY_BONUS = [
                        "+2 Strength",
                        "+2 Dexterity",
                        "+2 Constitution",
                        "+2 Intelligence",
                        "+2 Wisdom",
                        "+2 Charisma"
                    ]

    ALIGNMENTS = ["","LG","NG","CG","LN","TN","CN","LE","NE","CE"]

    def __init__(self, view, char):
        self.view        = view
        self.char        = char
        self.classFrames = []

        self.charName     = StringVar()
        self.buyPoints    = IntVar(value=0)
        self.maxBuyPoints = IntVar(value=15)
        self.purchaseMode = StringVar(value="Standard Fantasy (15 points)")
        self.bonusAbility = StringVar(value="Choose ability bonus")
        self.alignment    = StringVar(value="Choose alignment")
        self.strBonusStr  = StringVar(value="STR (+0)")
        self.dexBonusStr  = StringVar(value="DEX (+0)")
        self.conBonusStr  = StringVar(value="CON (+0)")
        self.intBonusStr  = StringVar(value="INT (+0)")
        self.wisBonusStr  = StringVar(value="WIS (+0)")
        self.chaBonusStr  = StringVar(value="CHA (+0)")
        self.charClass    = StringVar(value="Choose class")
        self.levelNb      = IntVar(value=1)

        # Data
        self.race_data = json.load(open("data/races.json"))
        for race in self.race_data["races"]:
            self.RACES.append(race)

        self.RACES.sort()

        self.class_data = json.load(open("data/classes.json"))
        for className in self.class_data["classes"]:
            self.CLASSES.append(className)

        self.CLASSES.sort()

        # Tracing
        self.char.str.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.str))
        self.char.dex.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.dex))
        self.char.con.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.con))
        self.char.int.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.int))
        self.char.wis.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.wis))
        self.char.cha.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.cha))
        self.bonusAbility.trace("w", self.updateBonusAbility)
        self.purchaseMode.trace("w", lambda i,x,o: self.changePurchaseMode(self.purchaseMode.get()))
        self.charName.trace("w", lambda i,x,o: self.char.charName.set(self.charName.get()))
        self.char.race.trace("w", self.updateRace)
        self.alignment.trace("w", self.updateAlignment)
        self.char.charLevel.trace("w", self.updateAlignment)
        self.char.charLevel.trace("w", self.updateAbilityAdvancement)
        self.char.favClass.trace("w", self.updateFavClass)
        self.charClass.trace("w", lambda i,x,o: self.char.removeError(self.classError))


    def addInitialErrors(self):
        self.raceError     = self.char.addError(self.char.race, "Choose a race", self.view.racesMenu)
        self.buyPointError = self.char.addError(self.view.purchaseModeMenu, "Buy points remain to be spent", self.view.purchaseModeMenu)
        self.classError    = self.char.addError(self.charClass, "Choose a class", self.view.classMenu)


    def updateAbilityBonusString(self, stat):
        sign = "+" if stat.bonus.get() >= 0 else ""
        eval("self." + stat.shortName + "BonusStr").set(stat.shortName.upper() + " (" + sign + "%d)" % stat.bonus.get())


    def changePurchaseMode(self, purchaseMode):
        if purchaseMode == "Low Fantasy (10 points)":
            self.maxBuyPoints.set(10)
        elif purchaseMode == "Standard Fantasy (15 points)":
            self.maxBuyPoints.set(15)
        elif purchaseMode == "High Fantasy (20 points)":
            self.maxBuyPoints.set(20)
        else:
            self.maxBuyPoints.set(25)

        self.checkBuyPoints()


    def updateAbilityScore(self, stat, value):
        charStat = eval("self.char." + stat)
        current = charStat.baseValue.get()
        new = current + value

        if new >= 7 and new <= 18:
            charStat.baseValue.set(new)
            charStat.update()

            previousPoints = self.POINT_BUY_CHART[current]
            self.buyPoints.set(self.buyPoints.get() - previousPoints)

            points = self.POINT_BUY_CHART[new]
            self.buyPoints.set(self.buyPoints.get() + points)

            self.checkBuyPoints()


    def checkBuyPoints(self):
        self.char.removeError(self.buyPointError)
        
        if self.maxBuyPoints.get() < self.buyPoints.get():
            msg = "Too many buy points spent"
        elif self.maxBuyPoints.get() > self.buyPoints.get():
            msg = "Buy points remain to be spent"
        else:
            return

        self.buyPointError = self.char.addError(self.view.purchaseModeMenu, msg, self.view.purchaseModeMenu)


    def updateAbilityAdvancement(self,i,o,x):
        pass


    def updateRace(self,i,o,x):
        race = self.char.race.get()
        data = self.race_data["races"][race]

        self.char.removeMods("race")
        self.char.removeError(self.raceError)

        for mod in data["mods"]:
            target = eval("self.char." + mod["target"])
            self.char.modifiers[target][mod["type"]]["race"] = mod["value"]
            target.update()

        if race in self.HUMANLIKE_RACES:
            self.view.abilityMenu.grid()
            self.updateBonusAbility(i,o,x)
        else:
            self.view.abilityMenu.grid_remove()
            try:
                self.char.removeError(self.bonusAbilityError)
            except:
                pass

    def updateBonusAbility(self,i,o,x):
        bonus = self.bonusAbility.get()

        if bonus != "Choose ability bonus":
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
            
            self.char.removeMods("race")
            target = eval("self.char." + stat)
            self.char.modifiers[target]["racial"]["race"] = 2
            target.update()
            self.char.removeError(self.bonusAbilityError)
        else:
            self.bonusAbilityError = self.char.addError(self.bonusAbility, "Choose racial ability bonus", self.view.abilityMenu)
    

    def updateLevelNb(self, value):
        current   = self.levelNb.get()
        new       = current + value
        remaining = self.char.MAX_LEVEL - self.char.charLevel.get()

        if new >= 1 and new <= remaining:
            self.levelNb.set(new) 


    def addLevels(self):
        if self.charClass.get() == "Choose class":
            return
        else:
            currentLvl = self.char.charLevel.get()

            if currentLvl == 0 and self.char.favClass.get() == "Choose favorite class":
                self.favClassError = self.char.addError(self.char.favClass.get(), "Choose a favorite class", self.view.favClassMenu)
                self.view.favClassMenu.grid()

            for i in range(currentLvl, currentLvl + self.levelNb.get()):
                frame = self.view.createLevelFrame(i)
                self.classFrames.append(frame)
            
            self.char.charLevel.set(currentLvl + self.levelNb.get())
            if self.char.charLevel.get() == self.char.MAX_LEVEL:
                self.view.addLevelsButton.config(state="disabled")

            self.levelNb.set(1)


    def removeLevel(self,frame):
        level = frame.winfo_children()[0].cget("text")
        self.classFrames.remove(frame)
        self.char.removeLevel(int(level) - 1)
        frame.destroy()

        for i in range(0, len(self.classFrames)):
            current = self.classFrames[i]
            current.winfo_children()[0].config(text=i+1)

            if i == 0:
                for widget in current.winfo_children():
                    try:
                        if widget.removeMe:
                            widget.destroy()
                    except:
                        pass

                classStr = current.winfo_children()[1].cget("text")
                label = Label(current, text=self.class_data["classes"][classStr]["hitDie"], width=2, font=('Helvetica', 12))
                label.grid(row=0, column=3, padx=20)
                label.removeMe = True

        self.view.addLevelsButton.config(state="normal")
        if self.char.charLevel.get() == 0 and self.char.favClass.get() == "Choose favorite class":
            self.char.removeError(self.favClassError)
            self.view.favClassMenu.grid_remove()


    def updateAlignment(self,i,o,x):
        for charClass in self.classFrames:
            className = charClass.winfo_children()[1]
            className.config(fg="black")

            alignmentArray = self.class_data["classes"][className.cget("text")]["alignment"]

            error = self.char.findErrorBySource(className.cget("text"))
            if error != None:
                self.char.removeError(error)

            if len(alignmentArray) > 0 and self.alignment.get() not in alignmentArray:
                className.config(fg="red")
                message = self.class_data["classes"][className.cget("text")]["alignmentMsg"]
                self.char.addError(className.cget("text"), message, self.view.alignmentMenu)


    def updateFavClass(self,i,o,x):
        self.char.removeError(self.favClassError)
        for level in self.char.levels:
            if level.charClass != self.char.favClass.get():
                level.favClassBonusMenu.grid_remove()
                level.active.set(False)
            else:
                level.favClassBonusMenu.grid()
                level.active.set(True)

        self.char.checkFavClassBonuses()