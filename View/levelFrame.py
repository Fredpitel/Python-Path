#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as  tk

class LevelFrame():
    FAVORED_OPTIONS = ["+1 Hit Point", "+1 Skill Point"]

    def __init__(self, parent, controller, levelNumber, charClass, hitDie, isFavClass):
        self.controller    = controller 

        self.levelNumber   = tk.IntVar(value=levelNumber + 1)
        self.charClass     = tk.StringVar(value=charClass)
        self.hitDie        = tk.IntVar(value=hitDie)
        self.hp            = tk.StringVar(value="1")
        self.favClassBonus = tk.StringVar(value="Choose Bonus")
        self.isFavClass    = tk.BooleanVar(value=isFavClass)
        self.hpGained      = tk.IntVar(value=1)
        self.bonusChosen   = None

        self.frame = ttk.Frame(parent, relief=tk.SUNKEN)
        self.frame.pack(fill="x")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)

        self.hpLabel = tk.Label(self.frame, textvariable=self.hitDie, width=2, font=('Helvetica', 12))
        self.hpEntry = tk.Entry(self.frame, width=2, textvariable=self.hp, validate="key", font=('Helvetica', 12))

        self.checkFirstLevel()

        tk.Label(self.frame, textvariable=self.levelNumber, width=2, font=('Helvetica', 12)).grid(row=0, column=0, padx=5, sticky="W")
        self.classLabel = tk.Label(self.frame, textvariable=self.charClass, width=15, font=('Helvetica', 12))
        self.classLabel.grid(row=0, column=1, sticky="W")

        tk.Label(self.frame, text="HP: ", font=('Helvetica', 12)).grid(row=0, column=2, sticky="W")

        self.favClassBonusMenu = tk.OptionMenu(self.frame, self.favClassBonus, *self.FAVORED_OPTIONS)
        self.favClassBonusMenu.config(width=35, font=('Helvetica', 12), highlightthickness=0)
        self.favClassBonusMenu.grid(row=0, column=4, sticky="EW")

        if not self.isFavClass.get():
            self.favClassBonusMenu.config(state="disabled")

        self.button = tk.Button(self.frame, text="×", command=lambda: controller.removeLevel(self))
        self.button.grid(row=0, column=5, padx=5, pady=2, sticky="E")
        self.button.config(fg="red", font=('Helvetica', 12))

        self.levelNumber.trace(  "w", lambda i,o,x: self.checkFirstLevel())
        self.hp.trace(           "w", lambda i,o,x: self.validateEntry())
        self.favClassBonus.trace("w", lambda i,o,x: self.setFavClassBonus())
        self.isFavClass.trace(   "w", lambda i,o,x: self.toggleFavClass())


    def validateEntry(self):
        value = self.hp.get()

        if value == "":
            return
        else:
            try:
                value = int(value)
                if value  < 1:
                    value = "1"
                elif value > self.hitDie.get():
                    value = self.hitDie.get()
            except ValueError:
                value = self.hpGained.get()

        self.hp.set(value)
        self.hpGained.set(int(value))


    def toggleFavClass(self):
        if self.isFavClass.get():
            self.favClassBonusMenu.config(state="normal")
            if self.bonusChosen is not None:
                self.addFavClassBonus()
        else:
            self.favClassBonusMenu.config(state="disabled")
            if self.bonusChosen is not None:
                self.controller.controller.removeMod(self.favClassBonus, self.bonusChosen)


    def checkFirstLevel(self):
        if self.levelNumber.get() == 1:
            self.hpEntry.grid_remove()
            self.hpLabel.grid(row=0, column=3, sticky="W")
            self.hpGained.set(int(self.hitDie.get()))
        else:
            self.hpLabel.grid_remove()
            self.hpEntry.grid(row=0, column=3, sticky="W")


    def setFavClassBonus(self):
        if self.favClassBonus.get() == "+1 Hit Point":
            self.bonusChosen = "hp"
        elif self.favClassBonus.get() == "+1 Skill Point":
            self.bonusChosen = "skillPoints"
        else:
            # TODO
            return

        self.addFavClassBonus()


    def addFavClassBonus(self):    
        self.controller.controller.addMod({"target": self.bonusChosen, 
                                           "type": "untyped",
                                           "value": 1
                                           },
                                           self.favClassBonus,
                                           self.favClassBonusMenu)