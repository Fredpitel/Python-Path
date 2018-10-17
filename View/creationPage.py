#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

from advancementFrame import AdvancementFrame

class CreationPage():
	def __init__(self, controller, parent):
		self.controller = controller

		self.creationPage = ttk.Frame(parent, relief=tk.SUNKEN, padding=5)
		self.creationPage.grid_columnconfigure(0, weight=1)
		self.creationPage.grid_columnconfigure(1, weight=1)
		self.creationPage.grid_columnconfigure(2, weight=5)
		self.creationPage.grid_rowconfigure(1, weight=1)
		self.creationPage.grid(row=0, column=0, padx=5, sticky="NSEW")

		#
		# Left Frame
		#
		self.summaryFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.summaryFrame.grid(row=0, column=0, padx=10, sticky="NSEW")
		self.summaryFrame.grid_columnconfigure(1, weight=1)

		# Name
		tk.Label(self.summaryFrame, text="Character Name: ").grid(row=0, column=0)
		tk.Entry(self.summaryFrame, textvariable=self.controller.charName).grid(row=0, column=1, pady=10, sticky="EW")

		# Race
		tk.Label(self.summaryFrame, text="Race:").grid(row=1, column=0, pady=8)
		self.racesMenu = tk.OptionMenu(self.summaryFrame, self.controller.race, *self.controller.races)
		self.racesMenu.config(width=25, fg="red")
		self.racesMenu.grid(row=1, column=1)
		self.racesMenu.config(font=('Helvetica', 10), highlightthickness=0)

		# Racial Ability Bonus
		tk.Label(self.summaryFrame, text="Racial ability bonus: ").grid(row=2, column=0, pady=8, padx=10)
		self.abilityMenu = tk.OptionMenu(self.summaryFrame, self.controller.bonusAbility, *self.controller.ABILITY_BONUS)
		self.abilityMenu.config(width=25, fg="red")
		self.abilityMenu.grid(row=2, column=1)
		self.abilityMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.abilityMenu.grid_remove()

		# Alignment
		tk.Label(self.summaryFrame, text="Alignment: ").grid(row=3, column=0, pady=8, padx=10)
		self.alignmentMenu = tk.OptionMenu(self.summaryFrame, self.controller.alignment, *self.controller.ALIGNMENTS)
		self.alignmentMenu.config(width=25)
		self.alignmentMenu.grid(row=3, column=1)
		self.alignmentMenu.config(font=('Helvetica', 10), highlightthickness=0)

		# Deity
		tk.Label(self.summaryFrame, text="Deity: ").grid(row=4, column=0, pady=8, padx=10)
		self.deityMenu = tk.OptionMenu(self.summaryFrame, self.controller.deity, *self.controller.deities)
		self.deityMenu.config(width=25)
		self.deityMenu.grid(row=4, column=1, columnspan=3)
		self.deityMenu.config(font=('Helvetica', 10), highlightthickness=0)


		# Favorite Class
		tk.Label(self.summaryFrame, text="Favorite Class: ").grid(row=5, column=0, pady=8, padx=10)
		self.favClassMenu = tk.OptionMenu(self.summaryFrame, self.controller.favClass, *self.controller.classes)
		self.favClassMenu.config(width=25)
		self.favClassMenu.grid(row=5, column=1)
		self.favClassMenu.config(font=('Helvetica', 10), highlightthickness=0)
		self.favClassMenu.grid_remove()


		#
		# Ability Advancement
		#
		self.advancementFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.advancementFrame.grid(row=1, column=0, padx=10, pady=10, sticky="NEW")
		self.advancementFrame.grid_columnconfigure(1, weight=1)

		tk.Label(self.advancementFrame, text="Ability Advancement").grid(row=0, column=0, columnspan=2, sticky="EW")
		tk.Label(self.advancementFrame, text="Level").grid(row=1, column=0, padx=10, pady=10)
		tk.Label(self.advancementFrame, text="Ability").grid(row=1, column=1, padx=10, pady=10)


		#
		# Center Frame
		#
		self.statFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.statFrame.grid(row=0, column=1, padx=10, sticky="NEW")
		self.statFrame.grid_columnconfigure(0, weight=1)
		self.statFrame.grid_columnconfigure(1, weight=1)

		# Ability Scores
		tk.Label(self.statFrame, text="Ability Scores").grid(row=0, column=0, columnspan=2,sticky="EW")

		self.abilityFrame = ttk.Frame(self.statFrame)
		self.abilityFrame.grid(row=1, column=0, columnspan=2, sticky="EW")
		self.abilityFrame.grid_columnconfigure(0, weight=1)
		self.abilityFrame.grid_columnconfigure(1, weight=1)
		self.abilityFrame.grid_columnconfigure(2, weight=1)
		self.abilityFrame.grid_columnconfigure(3, weight=1)
		self.abilityFrame.grid_columnconfigure(4, weight=1)
		self.abilityFrame.grid_columnconfigure(5, weight=1)

		# STRENGTH
		tk.Label(self.abilityFrame, textvariable=self.controller.strBonusStr, relief=tk.SUNKEN).grid(row=0, column=0, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("str"), bg="white", width=2).grid(row=1, column=0, sticky="E", padx=5)
		self.strButtons = ttk.Frame(self.abilityFrame)
		self.strButtons.grid(row=1, column=1, sticky="W")
		self.createStatsButtons(self.strButtons, "str")

		# DEXTERITY
		tk.Label(self.abilityFrame, textvariable=self.controller.dexBonusStr, relief=tk.SUNKEN).grid(row=0, column=2, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("dex"), bg="white", width=2).grid(row=1, column=2, sticky="E", padx=5)
		self.dexButtons = ttk.Frame(self.abilityFrame)
		self.dexButtons.grid(row=1, column=3, sticky="W")
		self.createStatsButtons(self.dexButtons, "dex")

		# CONSTITUTION
		tk.Label(self.abilityFrame, textvariable=self.controller.conBonusStr, relief=tk.SUNKEN).grid(row=0, column=4, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("con"), bg="white", width=2).grid(row=1, column=4, sticky="E", padx=5)
		self.conButtons = ttk.Frame(self.abilityFrame)
		self.conButtons.grid(row=1, column=5, sticky="W")
		self.createStatsButtons(self.conButtons, "con")
		
		# INTELLIGENCE
		tk.Label(self.abilityFrame, textvariable=self.controller.intBonusStr, relief=tk.SUNKEN).grid(row=2, column=0, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("int"), bg="white", width=2).grid(row=3, column=0, sticky="E", padx=5)
		self.intButtons = ttk.Frame(self.abilityFrame)
		self.intButtons.grid(row=3, column=1, sticky="W")
		self.createStatsButtons(self.intButtons, "int")

		# WISDOM
		tk.Label(self.abilityFrame, textvariable=self.controller.wisBonusStr, relief=tk.SUNKEN).grid(row=2, column=2, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("wis"), bg="white", width=2).grid(row=3, column=2, sticky="E", padx=5)
		self.wisButtons = ttk.Frame(self.abilityFrame)
		self.wisButtons.grid(row=3, column=3, sticky="W")
		self.createStatsButtons(self.wisButtons, "wis")

		# CHARISMA
		tk.Label(self.abilityFrame, textvariable=self.controller.chaBonusStr, relief=tk.SUNKEN).grid(row=2, column=4, columnspan=2, pady=10)
		tk.Label(self.abilityFrame, textvariable=self.controller.getModifiableValue("cha"), bg="white", width=2).grid(row=3, column=4, sticky="E", padx=5)
		self.chaButtons = ttk.Frame(self.abilityFrame)
		self.chaButtons.grid(row=3, column=5, sticky="W")
		self.createStatsButtons(self.chaButtons, "cha")

		# BUY POINTS
		tk.Label(self.statFrame, text="Purchase Mode:").grid(row=2, column=0, pady=20)

		self.purchaseModeMenu = tk.OptionMenu(self.statFrame, self.controller.purchaseMode, *self.controller.PURCHASE_MODES)
		self.purchaseModeMenu.grid(row=2, column=1)
		self.purchaseModeMenu.config(width=25, font=('Helvetica', 10), highlightthickness=0)
		tk.Label(self.statFrame, text="Buy Points spent:").grid(row=3, column=0)
		self.buyPointsLabel = tk.Label(self.statFrame, textvariable=self.controller.buyPoints)
		self.buyPointsLabel.grid(row=3, column=1)

		# Languages
		self.languageFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.languageFrame.grid(row=1, column=1, rowspan=2, padx=10, pady=10, sticky="NEW")
		self.languageFrame.grid_columnconfigure(0, weight=1)

		tk.Label(self.languageFrame, text="Languages").grid(row=0, column=0, sticky="EW")
		self.addLanguageButton = tk.Button(self.languageFrame, text="Add", font=("helvetica", 10), command=self.controller.createLanguageWindow)
		self.addLanguageButton.grid(row=0, column=1, padx=10)
		self.addLanguageButton.config(state="disabled")

		self.knownLanguagesFrame = ttk.Frame(self.languageFrame, padding=5)
		self.knownLanguagesFrame.grid(row=1, column=0, columnspan=2, padx=5, sticky="EW")


		#
		# Right Frame
		#
		self.classFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.classFrame.grid(row=0, column=2, rowspan=3, padx=10, sticky="NEW")
		self.classFrame.grid_columnconfigure(1, weight=1)
		
		# Class
		tk.Label(self.classFrame, text="Class: ").grid(row=0, column=0, pady=8)
		self.classMenu = tk.OptionMenu(self.classFrame, self.controller.charClass, *self.controller.classes)
		self.classMenu.config(width=25)
		self.classMenu.grid(row=0, column=1, padx=10)
		self.classMenu.config(font=('Helvetica', 12), highlightthickness=0)

		tk.Label(self.classFrame, text="Level: ").grid(row=1, column=0)

		self.addLevelFrame = ttk.Frame(self.classFrame)
		self.addLevelFrame.grid(row=1, column=1, pady=8)
		tk.Label(self.addLevelFrame, textvariable=self.controller.levelNb, bg="white", width=2).grid(row=0, column=0, padx=10)

		self.lvlButtons = ttk.Frame(self.addLevelFrame)
		self.lvlButtons.grid(row=0, column=1)
		tk.Button(self.lvlButtons, text="▲", font=("helvetica", 6), width=1, command=lambda: self.controller.setLevelNb(1)).grid(row=0, column=0)
		tk.Button(self.lvlButtons, text="▼", font=("helvetica", 6), width=1, command=lambda: self.controller.setLevelNb(-1)).grid(row=1, column=0)
		self.addLevelsButton = tk.Button(self.addLevelFrame, text="Add level(s)", font=('Helvetica', 12), command=self.controller.addLevels)
		self.addLevelsButton.grid(row=0, column=2, padx=5, sticky="W")
		self.addLevelsButton.config(state="disabled")

		self.charClassFrame = ttk.Frame(self.classFrame)
		self.charClassFrame.grid(row=2, column=0, columnspan=2, sticky="NEW")

		# Total HP
		self.hpFrame = ttk.Frame(self.creationPage, relief=tk.RAISED, padding=5)
		self.hpFrame.grid(row=2, column=2, padx=10, sticky="SEW")
		self.hpFrame.grid_columnconfigure(1, weight=1)

		tk.Label(self.hpFrame, text="Hit Point(s):").grid(row=1, column=0)
		tk.Label(self.hpFrame, textvariable=self.controller.getModifiableValue("hp")).grid(row=1, column=1)

		self.creationPage.update_idletasks()


	def createStatsButtons(self, parent, stat):
		commandUp = lambda: self.controller.setAbilityScore(stat, 1)
		tk.Button(parent, text="▲", font=("helvetica", 6), width=1, command=commandUp).grid(row=0, column=0)

		commandDown = lambda: self.controller.setAbilityScore(stat, -1)
		tk.Button(parent, text="▼", font=("helvetica", 6), width=1, command=commandDown).grid(row=1, column=0)


	def addLanguageFrame(self, language, racial):
		frame = ttk.Frame(self.knownLanguagesFrame, relief=tk.SUNKEN)
		frame.grid_columnconfigure(0, weight=1)
		frame.language = language

		label = tk.Label(frame, text=language)
		label.config(font=('Helvetica', 10))
		label.grid(row=0, column=0, sticky="W", padx=5, pady=5)
		button = tk.Button(frame, text="×", command=lambda f=frame: self.controller.removeLanguage(f))
		button.config(fg="red", font=('Helvetica', 12))
		button.grid(row=0, column=1, sticky="E")
		if racial:
			button.config(state="disabled")

		frame.pack(fill="x")
		frame.racial = racial

		return frame
