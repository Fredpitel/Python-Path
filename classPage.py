#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import json
import tkinter as tk

from tkinter  import *

class ClassPage:
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

	def __init__(self, nb, char):
		self.char = char
		self.buyPoints = IntVar(value=0)
		self.maxBuyPoints = IntVar(value=15)
		self.purchaseMode = StringVar(value="Standard Fantasy (15 points)")
		self.purchaseMode.trace("w", lambda i,x,o: self.changePurchaseMode(self.purchaseMode.get()))
		
		self.strBonusStr = StringVar(value="STR (+0)")
		self.dexBonusStr = StringVar(value="DEX (+0)")
		self.conBonusStr = StringVar(value="CON (+0)")
		self.intBonusStr = StringVar(value="INT (+0)")
		self.wisBonusStr = StringVar(value="WIS (+0)")
		self.chaBonusStr = StringVar(value="CHA (+0)")

		classPage = ttk.Frame(nb, relief=RIDGE, padding=10)
		classPage.grid_rowconfigure(0, weight=1)
		classPage.grid_columnconfigure(0, weight=1)
		classPage.grid_columnconfigure(1, weight=1)
		classPage.grid_columnconfigure(2, weight=1)
		nb.add(classPage, text='Class(es)', padding=10)

		self.char.str.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.str))
		self.char.dex.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.dex))
		self.char.con.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.con))
		self.char.int.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.int))
		self.char.wis.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.wis))
		self.char.cha.bonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.cha))

		self.race_data = json.load(open("data/races.json"))
		for race in self.race_data["races"]:
			self.RACES.append(race)

		self.RACES.sort()

		self.class_data = json.load(open("data/classes.json"))
		for charClass in self.class_data["classes"]:
			self.CLASSES.append(charClass)

		self.CLASSES.sort()

		self.charClasses = []

		#
		# Left Frame
		#
		
		# Errors
		self.char.errorFrame = ttk.Frame(classPage, relief=SUNKEN, padding=10)
		self.char.errorFrame.grid(row=1, column=0, padx=10, sticky="NEW")
		self.char.errorFrame.grid_columnconfigure(1, weight=1)

		self.summaryFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.summaryFrame.grid(row=0, column=0, rowspan=2, padx=10, sticky="NEW")
		self.summaryFrame.grid_columnconfigure(1, weight=1)

		# Name
		Label(self.summaryFrame, text="Character Name: ").grid(row=0, column=0)

		self.charName = StringVar()
		self.charName.trace("w", lambda i,x,o: self.char.charName.set(self.charName.get()))
		Entry(self.summaryFrame, textvariable=self.charName).grid(row=0, column=1, pady=10, sticky="EW")

		# Race
		Label(self.summaryFrame, text="Race:").grid(row=1, column=0, pady=8)
		self.racesMenu = OptionMenu(self.summaryFrame, self.char.race, *self.RACES)
		self.racesMenu.config(width=25, fg="red")
		self.racesMenu.grid(row=1, column=1, columnspan=3)
		self.racesMenu.config(font=('Helvetica', 10), highlightthickness=0)

		self.char.race.trace("w", self.updateRace)
		self.raceError = self.char.addError(self.char.race, "Choose a race", self.racesMenu)

		Label(self.summaryFrame, text="Racial ability bonus: ").grid(row=2, column=0, pady=8, padx=10)
		self.bonusAbility = StringVar(value="Choose ability bonus")
		self.abilityMenu = OptionMenu(self.summaryFrame, self.bonusAbility, *self.ABILITY_BONUS)
		self.abilityMenu.config(width=25, fg="red")
		self.abilityMenu.grid(row=2, column=1, columnspan=3)
		self.abilityMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.abilityMenu.grid_remove()

		self.bonusAbility.trace("w", self.updateBonusAbility)

		# Alignment
		Label(self.summaryFrame, text="Alignment: ").grid(row=3, column=0, pady=8, padx=10)
		self.alignment = StringVar(value="Choose alignment")
		self.alignmentMenu = OptionMenu(self.summaryFrame, self.alignment, *self.ALIGNMENTS)
		self.alignmentMenu.config(width=25)
		self.alignmentMenu.grid(row=3, column=1, columnspan=3)
		self.alignmentMenu.config(font=('Helvetica', 10), highlightthickness=0)

		self.alignment.trace("w", self.updateAlignment)
		self.char.charLevel.trace("w", self.updateAlignment)
		self.char.charLevel.trace("w", self.updateAbilityAdvancement)

		Label(self.summaryFrame, text="Favorite Class: ").grid(row=4, column=0, pady=8, padx=10)
		self.favClassMenu = OptionMenu(self.summaryFrame, self.char.favClass, *self.CLASSES)
		self.favClassMenu.config(width=25)
		self.favClassMenu.grid(row=4, column=1, columnspan=3)
		self.favClassMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.favClassMenu.grid_remove()

		self.char.favClass.trace("w", self.updateFavClass)


		#
		# Center Frame
		#
		self.statFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.statFrame.grid(row=0, column=1, rowspan=2, padx=10, sticky="NEW")
		self.statFrame.grid_columnconfigure(0, weight=1)
		self.statFrame.grid_columnconfigure(1, weight=1)
		self.statFrame.grid_columnconfigure(2, weight=1)
		self.statFrame.grid_columnconfigure(3, weight=1)
		self.statFrame.grid_columnconfigure(4, weight=1)
		self.statFrame.grid_columnconfigure(5, weight=1)

		# Ability Scores
		Label(self.statFrame, text="Ability Scores").grid(row=0, column=0, columnspan=6)

		# STRENGTH
		Label(self.statFrame, textvariable=self.strBonusStr, relief=SUNKEN).grid(row=1, column=0, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.str.value, bg="white", width=2).grid(row=2, column=0, sticky="E", padx=5)
		self.strButtons = ttk.Frame(self.statFrame)
		self.strButtons.grid(row=2, column=1, sticky="W")
		self.createStatsButtons(self.strButtons, "str")

		# DEXTERITY
		Label(self.statFrame, textvariable=self.dexBonusStr, relief=SUNKEN).grid(row=1, column=2, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.dex.value, bg="white", width=2).grid(row=2, column=2, sticky="E", padx=5)
		self.dexButtons = ttk.Frame(self.statFrame)
		self.dexButtons.grid(row=2, column=3, sticky="W")
		self.createStatsButtons(self.dexButtons, "dex")

		# CONSTITUTION
		Label(self.statFrame, textvariable=self.conBonusStr, relief=SUNKEN).grid(row=1, column=4, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.con.value, bg="white", width=2).grid(row=2, column=4, sticky="E", padx=5)
		self.conButtons = ttk.Frame(self.statFrame)
		self.conButtons.grid(row=2, column=5, sticky="W")
		self.createStatsButtons(self.conButtons, "con")
		
		# INTELLIGENCE
		Label(self.statFrame, textvariable=self.intBonusStr, relief=SUNKEN).grid(row=3, column=0, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.int.value, bg="white", width=2).grid(row=4, column=0, sticky="E", padx=5)
		self.intButtons = ttk.Frame(self.statFrame)
		self.intButtons.grid(row=4, column=1, sticky="W")
		self.createStatsButtons(self.intButtons, "int")

		# WISDOM
		Label(self.statFrame, textvariable=self.wisBonusStr, relief=SUNKEN).grid(row=3, column=2, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.wis.value, bg="white", width=2).grid(row=4, column=2, sticky="E", padx=5)
		self.wisButtons = ttk.Frame(self.statFrame)
		self.wisButtons.grid(row=4, column=3, sticky="W")
		self.createStatsButtons(self.wisButtons, "wis")

		# CHARISMA
		Label(self.statFrame, textvariable=self.chaBonusStr, relief=SUNKEN).grid(row=3, column=4, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.cha.value, bg="white", width=2).grid(row=4, column=4, sticky="E", padx=5)
		self.chaButtons = ttk.Frame(self.statFrame)
		self.chaButtons.grid(row=4, column=5, sticky="W")
		self.createStatsButtons(self.chaButtons, "cha")

		# BUY POINTS
		Label(self.statFrame, text="Purchase Mode:").grid(row=5, column=0, columnspan=3, pady=20)

		self.purchaseModeMenu = OptionMenu(self.statFrame, self.purchaseMode, *self.PURCHASE_MODES)
		self.purchaseModeMenu.grid(row=5, column=3, columnspan=3)
		self.purchaseModeMenu.config(font=('Helvetica', 10), highlightthickness=0)
		Label(self.statFrame, text="Buy Points spent:").grid(row=6, column=0, columnspan=3)
		Label(self.statFrame, textvariable=self.buyPoints).grid(row=6, column=3, columnspan=3)

		self.buyPointError = self.char.addError(self.purchaseModeMenu, "Buy points remain to be spent", self.purchaseModeMenu)

		#
		# Right Frame
		#
		self.classFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.classFrame.grid(row=0, column=2, padx=10, sticky="NEW")
		self.classFrame.grid_columnconfigure(1, weight=1)
		
		# Class
		Label(self.classFrame, text="Class: ").grid(row=0, column=0, pady=8)
		self.charClass = StringVar(value="Choose class")
		self.classMenu = OptionMenu(self.classFrame, self.charClass, *self.CLASSES)
		self.classMenu.config(width=25)
		self.classMenu.grid(row=0, column=1)
		self.classMenu.config(font=('Helvetica', 12), highlightthickness=0)

		self.charClass.trace("w", lambda i,x,o: self.classMenu.config(fg="black"))

		Label(self.classFrame, text="Level: ").grid(row=1, column=0)

		self.addLevelFrame = ttk.Frame(self.classFrame)
		self.addLevelFrame.grid(row=1, column=1, pady=8)
		self.levelNb = IntVar(value=1)
		Label(self.addLevelFrame, textvariable=self.levelNb, bg="white", width=2).grid(row=0, column=0, padx=10)

		self.lvlButtons = ttk.Frame(self.addLevelFrame)
		self.lvlButtons.grid(row=0, column=1)
		Button(self.lvlButtons, text="▲", font=("helvetica", 6), width=1, command=lambda: self.updateLevelNb(1)).grid(row=0, column=0)
		Button(self.lvlButtons, text="▼", font=("helvetica", 6), width=1, command=lambda: self.updateLevelNb(-1)).grid(row=1, column=0)
		self.addLevelsButton = Button(self.addLevelFrame, text="Add level(s)", font=('Helvetica', 12), command=self.addLevels)
		self.addLevelsButton.grid(row=0, column=2, padx=5, sticky="W")

		self.charClassFrame = ttk.Frame(self.classFrame)
		self.charClassFrame.grid(row=2, column=0, columnspan=2)

		# Total HP
		self.hpFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.hpFrame.grid(row=1, column=2, padx=10, sticky="NEW")
		self.hpFrame.grid_columnconfigure(1, weight=1)

		Label(self.hpFrame, text="Hit Point(s):").grid(row=1, column=0)
		Label(self.hpFrame, textvariable=self.char.hp.value).grid(row=1, column=1)


	def updateAbilityBonusString(self, stat):
		sign = "+" if stat.bonus.get() >= 0 else ""
		eval("self." + stat.shortName + "BonusStr").set(stat.shortName.upper() + " (" + sign + "%d)" % stat.bonus.get())


	def createStatsButtons(self, parent, stat):
		commandUp = lambda: self.updateAbilityScore(stat, 1)
		Button(parent, text="▲", font=("helvetica", 6), width=1, command=commandUp).grid(row=0, column=0)

		commandDown = lambda: self.updateAbilityScore(stat, -1)
		Button(parent, text="▼", font=("helvetica", 6), width=1, command=commandDown).grid(row=1, column=0)


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

		if self.maxBuyPoints.get() == self.buyPoints.get():
			self.purchaseModeMenu.config(fg="green")
			return
		elif self.maxBuyPoints.get() < self.buyPoints.get():
			msg = "Too many buy points spent"
		else:
			msg = "Buy points remain to be spent"

		self.buyPointError = self.char.addError(self.purchaseModeMenu, msg, self.purchaseModeMenu)


	def updateAbilityAdvancement(self,i,o,x):
		pass


	def updateRace(self,i,o,x):
		race = self.char.race.get()
		data = self.race_data["races"][race]

		self.char.removeMods("race")
		self.char.removeError(self.raceError)
		self.racesMenu.config(fg="black")

		for mod in data["mods"]:
			target = eval("self.char." + mod["target"])
			self.char.modifiers[target][mod["type"]]["race"] = mod["value"]
			target.update()

		if race in self.HUMANLIKE_RACES:
			self.abilityMenu.grid()
			self.updateBonusAbility(i,o,x)
		else:
			self.abilityMenu.grid_remove()
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
			self.bonusAbilityError = self.char.addError(self.bonusAbility, "Choose racial ability bonus", self.abilityMenu)
	
		

	def updateLevelNb(self, value):
		current   = self.levelNb.get()
		new       = current + value
		remaining = self.char.MAX_LEVEL - self.char.charLevel.get()

		if new >= 1 and new <= remaining:
			self.levelNb.set(new) 


	def addLevels(self):
		if self.charClass.get() == "Choose class":
			self.classMenu.config(fg="red")
			return
		else:
			self.classMenu.config(fg="black")

			currentLvl = self.char.charLevel.get()

			for i in range(currentLvl, currentLvl + self.levelNb.get()):
				newFrame = ttk.Frame(self.charClassFrame, relief=SUNKEN)
				newFrame.pack(fill="x")
				newFrame.grid_columnconfigure(5, weight=1)
				
				Label(newFrame, text=str(i + 1), width=2, font=('Helvetica', 12)).grid(row=0, column=0, padx=20)
				Label(newFrame, text=self.charClass.get(), font=('Helvetica', 12), width=12).grid(row=0, column=1, padx=20)

				Label(newFrame, text="HP: ", font=('Helvetica', 12)).grid(row=0, column=2)

				hitDie = self.class_data["classes"][self.charClass.get()]["hitDie"]
				if i == 0:
					hp = StringVar(value=str(hitDie))
					label = Label(newFrame, textvariable=hp, width=2, font=('Helvetica', 12))
					label.grid(row=0, column=3, padx=20)
					label.removeMe = True
				
				else:
					hp = StringVar(value="1")
					Entry(newFrame, width=2, textvariable=hp, validate="key", font=('Helvetica', 12)).grid(row=0, column=3, padx=20)

				favClassBonusOption = ["+1 Hit Point", "+1 Skill Point"]
				favClassBonus = StringVar(value="Choose Bonus")
				favClassBonusMenu = OptionMenu(newFrame, favClassBonus, *favClassBonusOption)
				favClassBonusMenu.config(width=15, font=('Helvetica', 12), highlightthickness=0)
				favClassBonusMenu.grid(row=0, column=4)

				Button(newFrame, text="×", fg="red", font=('Helvetica', 12), relief=FLAT, command=lambda frame=newFrame:self.removeLevel(frame)).grid(row=0, column=5,pady=2, padx=20, sticky="E")

				self.charClasses.append(newFrame)
				self.char.addLevel(self.charClass.get(), hp, hitDie, favClassBonus, favClassBonusMenu)
			
			self.char.charLevel.set(currentLvl + self.levelNb.get())
			if self.char.charLevel.get() == self.char.MAX_LEVEL:
				self.addLevelsButton.config(state="disabled")

			self.levelNb.set(1)
			if self.char.charLevel.get() == 1:
				self.favClassMenu.grid()
				if self.char.favClass.get() == "Choose favorite class":
					self.favClassError = self.char.addError(self.char.favClass.get(), "Choose a favorite class", self.favClassMenu)


	def removeLevel(self,frame):
		level = frame.winfo_children()[0].cget("text")
		self.charClasses.remove(frame)
		self.char.removeLevel(int(level) - 1)
		frame.destroy()

		for i in range(0, len(self.charClasses)):
			current = self.charClasses[i]
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

		self.addLevelsButton.config(state="normal")
		if self.char.charLevel.get() == 0:
			self.favClassMenu.grid_remove()


	def updateAlignment(self,i,o,x):
		for charClass in self.charClasses:
			className = charClass.winfo_children()[1]
			className.config(fg="black")

			alignmentArray = self.class_data["classes"][className.cget("text")]["alignment"]

			error = self.char.findErrorBySource(className.cget("text"))
			if error != None:
				self.char.removeError(error)

			if len(alignmentArray) > 0 and self.alignment.get() not in alignmentArray:
				className.config(fg="red")
				message = self.class_data["classes"][className.cget("text")]["alignmentMsg"]
				self.char.addError(className.cget("text"), message, self.alignmentMenu)


	def updateFavClass(self,i,o,x):
		self.char.removeError(self.favClassError)

		for level in self.char.levels:
			if level.charClass != self.char.favClass.get():
				level.favClassBonusMenu.grid_remove()
				level.active.set(False)
			else:
				level.favClassBonusMenu.grid()
				level.active.set(True)