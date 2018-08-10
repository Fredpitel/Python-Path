#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import json
import tkinter as tk

from tkinter  import *
from math     import *
from level    import Level


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

		self.char.strBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.strBonus.get(), "str"))
		self.char.dexBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.dexBonus.get(), "dex"))
		self.char.conBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.conBonus.get(), "con"))
		self.char.intBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.intBonus.get(), "int"))
		self.char.wisBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.wisBonus.get(), "wis"))
		self.char.chaBonus.trace("w", lambda i,x,o: self.updateAbilityBonusString(self.char.chaBonus.get(), "cha"))

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
		self.racesMenu.config(width=25)
		self.racesMenu.grid(row=1, column=1, columnspan=3)
		self.racesMenu.config(font=('Helvetica', 10), highlightthickness=0)

		self.char.race.trace("w", self.updateRace)

		Label(self.summaryFrame, text="Racial ability bonus: ").grid(row=2, column=0, pady=8, padx=10)
		self.bonusAbility = StringVar(value="Choose ability bonus")
		self.abilityMenu = OptionMenu(self.summaryFrame, self.bonusAbility, *self.ABILITY_BONUS)
		self.abilityMenu.config(width=25)
		self.abilityMenu.grid(row=2, column=1, columnspan=3)
		self.abilityMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.abilityMenu.grid_remove()

		self.bonusAbility.trace("w", self.updateBonusAbility)

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
		Label(self.statFrame, textvariable=self.char.str, bg="white", width=2).grid(row=2, column=0, sticky="E", padx=5)
		self.strButtons = ttk.Frame(self.statFrame)
		self.strButtons.grid(row=2, column=1, sticky="W")
		self.createStatsButtons(self.strButtons, "str")

		# DEXTERITY
		Label(self.statFrame, textvariable=self.dexBonusStr, relief=SUNKEN).grid(row=1, column=2, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.dex, bg="white", width=2).grid(row=2, column=2, sticky="E", padx=5)
		self.dexButtons = ttk.Frame(self.statFrame)
		self.dexButtons.grid(row=2, column=3, sticky="W")
		self.createStatsButtons(self.dexButtons, "dex")

		# CONSTITUTION
		Label(self.statFrame, textvariable=self.conBonusStr, relief=SUNKEN).grid(row=1, column=4, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.con, bg="white", width=2).grid(row=2, column=4, sticky="E", padx=5)
		self.conButtons = ttk.Frame(self.statFrame)
		self.conButtons.grid(row=2, column=5, sticky="W")
		self.createStatsButtons(self.conButtons, "con")
		
		# INTELLIGENCE
		Label(self.statFrame, textvariable=self.intBonusStr, relief=SUNKEN).grid(row=3, column=0, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.int, bg="white", width=2).grid(row=4, column=0, sticky="E", padx=5)
		self.intButtons = ttk.Frame(self.statFrame)
		self.intButtons.grid(row=4, column=1, sticky="W")
		self.createStatsButtons(self.intButtons, "int")

		# WISDOM
		Label(self.statFrame, textvariable=self.wisBonusStr, relief=SUNKEN).grid(row=3, column=2, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.wis, bg="white", width=2).grid(row=4, column=2, sticky="E", padx=5)
		self.wisButtons = ttk.Frame(self.statFrame)
		self.wisButtons.grid(row=4, column=3, sticky="W")
		self.createStatsButtons(self.wisButtons, "wis")

		# CHARISMA
		Label(self.statFrame, textvariable=self.chaBonusStr, relief=SUNKEN).grid(row=3, column=4, columnspan=2, pady=10)
		Label(self.statFrame, textvariable=self.char.cha, bg="white", width=2).grid(row=4, column=4, sticky="E", padx=5)
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


		#
		# Right Frame
		#
		self.classFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.classFrame.grid(row=0, column=2, padx=10, sticky="NEW")
		self.classFrame.grid_columnconfigure(1, weight=1)

		# Class
		Label(self.classFrame, text="Class: ").grid(row=2, column=0, pady=8)
		self.charClass = StringVar(value="Choose class")
		self.classMenu = OptionMenu(self.classFrame, self.charClass, *self.CLASSES)
		self.classMenu.config(width=25)
		self.classMenu.grid(row=2, column=1, columnspan=3)
		self.classMenu.config(font=('Helvetica', 12), highlightthickness=0)

		self.charClass.trace("w", lambda i,x,o: self.classMenu.config(fg="black"))

		Label(self.classFrame, text="Level: ").grid(row=3, column=0)

		self.addLevelFrame = ttk.Frame(self.classFrame)
		self.addLevelFrame.grid(row=3, column=1, pady=8)
		self.levelNb = IntVar(value=1)
		Label(self.addLevelFrame, textvariable=self.levelNb, bg="white", width=2).grid(row=0, column=0, padx=10)

		self.lvlButtons = ttk.Frame(self.addLevelFrame)
		self.lvlButtons.grid(row=0, column=1)
		Button(self.lvlButtons, text="▲", font=("helvetica", 6), width=1, command=lambda: self.updateLevelNb(1)).grid(row=0, column=0)
		Button(self.lvlButtons, text="▼", font=("helvetica", 6), width=1, command=lambda: self.updateLevelNb(-1)).grid(row=1, column=0)
		self.addLevelsButton = Button(self.addLevelFrame, text="Add level(s)", font=('Helvetica', 12), command=self.addLevels)
		self.addLevelsButton.grid(row=0, column=2, padx=5, sticky="W")

		self.charClassFrame = ttk.Frame(self.classFrame)
		self.charClassFrame.grid(row=4, column=0, columnspan=3)

		# Total HP
		self.hpFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.hpFrame.grid(row=1, column=2, padx=10, sticky="NEW")
		self.hpFrame.grid_columnconfigure(1, weight=1)

		Label(self.hpFrame, text="Hit Point(s):").grid(row=1, column=0)
		Label(self.hpFrame, textvariable=self.char.hp).grid(row=1, column=1)



	def updateAbilityBonusString(self, bonus, stat):
		sign = "+" if bonus >= 0 else ""
		eval("self." + stat + "BonusStr").set(stat.upper() + " (" + sign + "%d)" % bonus)


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
		current = eval("self.char." + stat + "Base").get()
		new = current + value

		if new >= 7 and new <= 18:
			eval("self.char." + stat + "Base").set(new)
			self.char.updateAbilityScore(stat)

			previousPoints = self.POINT_BUY_CHART[current]
			self.buyPoints.set(self.buyPoints.get() - previousPoints)

			points = self.POINT_BUY_CHART[new]
			self.buyPoints.set(self.buyPoints.get() + points)

			self.checkBuyPoints()


	def checkBuyPoints(self):
		if self.maxBuyPoints.get() < self.buyPoints.get():
			self.purchaseModeMenu.config(fg="red")
		elif self.maxBuyPoints.get() == self.buyPoints.get():
			self.purchaseModeMenu.config(fg="green")
		else:	
			self.purchaseModeMenu.config(fg="black")

	def updateRace(self,i,o,x):
		race = self.char.race.get()
		data = self.race_data["races"][race]

		self.char.removeMods("race")

		for mod in data["mods"]:
			self.char.modifiers[mod["target"]][mod["type"]]["race"] = mod["value"]
			self.char.updateMods(mod["target"])

		if race in self.HUMANLIKE_RACES:
			self.abilityMenu.grid()
			self.updateBonusAbility(i,o,x)
		else:
			self.abilityMenu.grid_remove()


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
			self.char.modifiers[stat]["racial"]["race"] = 2
			self.char.updateAbilityScore(stat)
		

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
				newFrame.pack(expand=True)

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

				Button(newFrame, text="×", fg="red", font=('Helvetica', 12), relief=FLAT, command=lambda frame=newFrame:self.removeLevel(frame)).grid(row=0, column=5,pady=2, padx=20)

				self.charClasses.append(newFrame)
				level = Level(self.char, self.charClass.get(), hp, hitDie, favClassBonus)
				self.char.levels.append(level)

			
			self.char.charLevel.set(currentLvl + self.levelNb.get())
			if self.char.charLevel.get() == self.char.MAX_LEVEL:
				self.addLevelsButton.config(state="disabled")

			self.levelNb.set(1)

	def removeLevel(self,frame):
		level = frame.winfo_children()[0].cget("text")
		self.charClasses.remove(frame)
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

		del self.char.levels[int(level) - 1]
		self.char.charLevel.set(self.char.charLevel.get() - 1)

		self.addLevelsButton.config(state="normal")