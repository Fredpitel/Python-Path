#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import tkinter as tk

from tkinter  import *
from classPageController import *

class ClassPage:
	def __init__(self, nb, char):
		self.char = char
		self.controller = classPageController(self, char)

		classPage = ttk.Frame(nb, relief=RIDGE, padding=10)
		classPage.grid_columnconfigure(0, weight=1)
		classPage.grid_columnconfigure(1, weight=1)
		classPage.grid_columnconfigure(2, weight=1)
		classPage.grid_rowconfigure(1, weight=1)
		nb.add(classPage, text='Class(es)', padding=10)

		#
		# Left Frame
		#
		self.summaryFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.summaryFrame.grid(row=0, column=0, padx=10, sticky="NEW")
		self.summaryFrame.grid_columnconfigure(1, weight=1)

		# Name
		Label(self.summaryFrame, text="Character Name: ").grid(row=0, column=0)
		Entry(self.summaryFrame, textvariable=self.controller.charName).grid(row=0, column=1, pady=10, sticky="EW")

		# Race
		Label(self.summaryFrame, text="Race:").grid(row=1, column=0, pady=8)
		self.racesMenu = OptionMenu(self.summaryFrame, self.char.race, *self.controller.RACES)
		self.racesMenu.config(width=25, fg="red")
		self.racesMenu.grid(row=1, column=1, columnspan=3)
		self.racesMenu.config(font=('Helvetica', 10), highlightthickness=0)

		Label(self.summaryFrame, text="Racial ability bonus: ").grid(row=2, column=0, pady=8, padx=10)
		self.abilityMenu = OptionMenu(self.summaryFrame, self.controller.bonusAbility, *self.controller.ABILITY_BONUS)
		self.abilityMenu.config(width=25, fg="red")
		self.abilityMenu.grid(row=2, column=1, columnspan=3)
		self.abilityMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.abilityMenu.grid_remove()

		# Alignment
		Label(self.summaryFrame, text="Alignment: ").grid(row=3, column=0, pady=8, padx=10)
		self.alignmentMenu = OptionMenu(self.summaryFrame, self.controller.alignment, *self.controller.ALIGNMENTS)
		self.alignmentMenu.config(width=25)
		self.alignmentMenu.grid(row=3, column=1, columnspan=3)
		self.alignmentMenu.config(font=('Helvetica', 10), highlightthickness=0)

		Label(self.summaryFrame, text="Favorite Class: ").grid(row=4, column=0, pady=8, padx=10)
		self.favClassMenu = OptionMenu(self.summaryFrame, self.char.favClass, *self.controller.CLASSES)
		self.favClassMenu.config(width=25)
		self.favClassMenu.grid(row=4, column=1, columnspan=3)
		self.favClassMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.favClassMenu.grid_remove()

		# Errors
		self.char.errorFrame = ttk.Frame(classPage, relief=SUNKEN, padding=10)
		self.char.errorFrame.grid(row=1, column=0, padx=10, sticky="SEW")
		self.char.errorFrame.grid_propagate(0)


		#
		# Center Frame
		#
		self.statFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.statFrame.grid(row=0, column=1, rowspan=2, padx=10, sticky="NEW")
		self.statFrame.grid_columnconfigure(0, weight=1)
		self.statFrame.grid_columnconfigure(1, weight=1)

		# Ability Scores
		Label(self.statFrame, text="Ability Scores").grid(row=0, column=0, columnspan=2,sticky="EW")

		self.abilityFrame = ttk.Frame(self.statFrame)
		self.abilityFrame.grid(row=1, column=0, columnspan=2, sticky="EW")
		self.abilityFrame.grid_columnconfigure(0, weight=1)
		self.abilityFrame.grid_columnconfigure(1, weight=1)
		self.abilityFrame.grid_columnconfigure(2, weight=1)
		self.abilityFrame.grid_columnconfigure(3, weight=1)
		self.abilityFrame.grid_columnconfigure(4, weight=1)
		self.abilityFrame.grid_columnconfigure(5, weight=1)

		# STRENGTH
		Label(self.abilityFrame, textvariable=self.controller.strBonusStr, relief=SUNKEN).grid(row=0, column=0, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.str.value, bg="white", width=2).grid(row=1, column=0, sticky="E", padx=5)
		self.strButtons = ttk.Frame(self.abilityFrame)
		self.strButtons.grid(row=1, column=1, sticky="W")
		self.createStatsButtons(self.strButtons, "str")

		# DEXTERITY
		Label(self.abilityFrame, textvariable=self.controller.dexBonusStr, relief=SUNKEN).grid(row=0, column=2, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.dex.value, bg="white", width=2).grid(row=1, column=2, sticky="E", padx=5)
		self.dexButtons = ttk.Frame(self.abilityFrame)
		self.dexButtons.grid(row=1, column=3, sticky="W")
		self.createStatsButtons(self.dexButtons, "dex")

		# CONSTITUTION
		Label(self.abilityFrame, textvariable=self.controller.conBonusStr, relief=SUNKEN).grid(row=0, column=4, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.con.value, bg="white", width=2).grid(row=1, column=4, sticky="E", padx=5)
		self.conButtons = ttk.Frame(self.abilityFrame)
		self.conButtons.grid(row=1, column=5, sticky="W")
		self.createStatsButtons(self.conButtons, "con")
		
		# INTELLIGENCE
		Label(self.abilityFrame, textvariable=self.controller.intBonusStr, relief=SUNKEN).grid(row=2, column=0, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.int.value, bg="white", width=2).grid(row=3, column=0, sticky="E", padx=5)
		self.intButtons = ttk.Frame(self.abilityFrame)
		self.intButtons.grid(row=3, column=1, sticky="W")
		self.createStatsButtons(self.intButtons, "int")

		# WISDOM
		Label(self.abilityFrame, textvariable=self.controller.wisBonusStr, relief=SUNKEN).grid(row=2, column=2, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.wis.value, bg="white", width=2).grid(row=3, column=2, sticky="E", padx=5)
		self.wisButtons = ttk.Frame(self.abilityFrame)
		self.wisButtons.grid(row=3, column=3, sticky="W")
		self.createStatsButtons(self.wisButtons, "wis")

		# CHARISMA
		Label(self.abilityFrame, textvariable=self.controller.chaBonusStr, relief=SUNKEN).grid(row=2, column=4, columnspan=2, pady=10)
		Label(self.abilityFrame, textvariable=self.char.cha.value, bg="white", width=2).grid(row=3, column=4, sticky="E", padx=5)
		self.chaButtons = ttk.Frame(self.abilityFrame)
		self.chaButtons.grid(row=3, column=5, sticky="W")
		self.createStatsButtons(self.chaButtons, "cha")

		# BUY POINTS
		Label(self.statFrame, text="Purchase Mode:").grid(row=2, column=0, pady=20)

		self.purchaseModeMenu = OptionMenu(self.statFrame, self.controller.purchaseMode, *self.controller.PURCHASE_MODES)
		self.purchaseModeMenu.grid(row=2, column=1)
		self.purchaseModeMenu.config(font=('Helvetica', 10), highlightthickness=0)
		Label(self.statFrame, text="Buy Points spent:").grid(row=3, column=0)
		Label(self.statFrame, textvariable=self.controller.buyPoints).grid(row=3, column=1)

		
		#
		# Right Frame
		#
		self.classFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.classFrame.grid(row=0, column=2, rowspan=2, padx=10, sticky="NEW")
		self.classFrame.grid_columnconfigure(1, weight=1)
		
		# Class
		Label(self.classFrame, text="Class: ").grid(row=0, column=0, pady=8)
		self.classMenu = OptionMenu(self.classFrame, self.controller.charClass, *self.controller.CLASSES)
		self.classMenu.config(width=25)
		self.classMenu.grid(row=0, column=1, padx=10)
		self.classMenu.config(font=('Helvetica', 12), highlightthickness=0)

		Label(self.classFrame, text="Level: ").grid(row=1, column=0)

		self.addLevelFrame = ttk.Frame(self.classFrame)
		self.addLevelFrame.grid(row=1, column=1, pady=8)
		Label(self.addLevelFrame, textvariable=self.controller.levelNb, bg="white", width=2).grid(row=0, column=0, padx=10)

		self.lvlButtons = ttk.Frame(self.addLevelFrame)
		self.lvlButtons.grid(row=0, column=1)
		Button(self.lvlButtons, text="▲", font=("helvetica", 6), width=1, command=lambda: self.controller.updateLevelNb(1)).grid(row=0, column=0)
		Button(self.lvlButtons, text="▼", font=("helvetica", 6), width=1, command=lambda: self.controller.updateLevelNb(-1)).grid(row=1, column=0)
		self.addLevelsButton = Button(self.addLevelFrame, text="Add level(s)", font=('Helvetica', 12), command=self.controller.addLevels)
		self.addLevelsButton.grid(row=0, column=2, padx=5, sticky="W")

		self.charClassFrame = ttk.Frame(self.classFrame)
		self.charClassFrame.grid(row=2, column=0, columnspan=2, sticky="NEW")

		# Total HP
		self.hpFrame = ttk.Frame(classPage, relief=RAISED, padding=10)
		self.hpFrame.grid(row=1, column=2, padx=10, sticky="SEW")
		self.hpFrame.grid_columnconfigure(1, weight=1)

		Label(self.hpFrame, text="Hit Point(s):").grid(row=1, column=0)
		Label(self.hpFrame, textvariable=self.char.hp.value).grid(row=1, column=1)

		self.controller.addInitialErrors()


	def createStatsButtons(self, parent, stat):
		commandUp = lambda: self.controller.updateAbilityScore(stat, 1)
		Button(parent, text="▲", font=("helvetica", 6), width=1, command=commandUp).grid(row=0, column=0)

		commandDown = lambda: self.controller.updateAbilityScore(stat, -1)
		Button(parent, text="▼", font=("helvetica", 6), width=1, command=commandDown).grid(row=1, column=0)


	def createLevelFrame(self, index):
		newFrame = ttk.Frame(self.charClassFrame, relief=SUNKEN)
		newFrame.pack(fill="x")
		newFrame.grid_columnconfigure(0, weight=1)
		newFrame.grid_columnconfigure(1, weight=1)
		newFrame.grid_columnconfigure(2, weight=1)
		newFrame.grid_columnconfigure(3, weight=1)
		newFrame.grid_columnconfigure(4, weight=1)
		newFrame.grid_columnconfigure(5, weight=1)
		
		Label(newFrame, text=str(index + 1), width=2, font=('Helvetica', 12)).grid(row=0, column=0, padx=5, sticky="W")
		Label(newFrame, text=self.controller.charClass.get(), font=('Helvetica', 12), width=12).grid(row=0, column=1, sticky="W")

		Label(newFrame, text="HP: ", font=('Helvetica', 12)).grid(row=0, column=2, sticky="W")

		hitDie = self.controller.class_data["classes"][self.controller.charClass.get()]["hitDie"]
		if index == 0:
			hp = StringVar(value=str(hitDie))
			label = Label(newFrame, textvariable=hp, width=2, font=('Helvetica', 12))
			label.grid(row=0, column=3, sticky="W")
			label.removeMe = True
		
		else:
			hp = StringVar(value="1")
			Entry(newFrame, width=2, textvariable=hp, validate="key", font=('Helvetica', 12)).grid(row=0, column=3, sticky="W")

		favClassBonusOption = ["+1 Hit Point", "+1 Skill Point"]
		favClassBonus = StringVar(value="Choose Bonus")
		favClassBonusMenu = OptionMenu(newFrame, favClassBonus, *favClassBonusOption)
		favClassBonusMenu.config(width=15, font=('Helvetica', 12), highlightthickness=0)
		favClassBonusMenu.grid(row=0, column=4, sticky="W")

		Button(newFrame, text="×", fg="red", font=('Helvetica', 12), relief=FLAT, command=lambda frame=newFrame:self.controller.removeLevel(frame)).grid(row=0, column=5, padx=5, pady=2, sticky="E")

		self.char.addLevel(self.controller.charClass.get(), hp, hitDie, favClassBonus, favClassBonusMenu)

		return newFrame
