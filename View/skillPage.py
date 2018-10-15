#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

class SkillPage:
    def __init__(self, controller, parent):
        self.controller = controller

        self.skillPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.skillPage.grid(row=0, column=0, sticky= "NSEW")
        self.skillPage.grid_rowconfigure(0, weight=1)
        self.skillPage.grid_rowconfigure(1, weight=1)
        self.skillPage.grid_columnconfigure(0, weight=1)

        self.skillFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=5)
        self.skillFrame.grid_columnconfigure(0, weight=1)
        self.skillFrame.grid_columnconfigure(1, weight=1)
        self.skillFrame.grid_columnconfigure(2, weight=1)
        self.skillFrame.grid_columnconfigure(3, weight=1)
        self.skillFrame.grid_columnconfigure(4, weight=1)
        self.skillFrame.grid_columnconfigure(5, weight=1)
        self.skillFrame.grid_columnconfigure(6, weight=1)
        self.skillFrame.grid_columnconfigure(7, weight=1)
        self.skillFrame.grid(row=0, column=0, sticky="NSEW")

        skillDict = self.controller.char.skill.skills
        skills = skillDict.keys()
        skills.sort()

        self.populateFrame(self.skillFrame, skillDict, skills)

        self.knowledgeFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=5)
        self.knowledgeFrame.grid_columnconfigure(0, weight=1)
        self.knowledgeFrame.grid_columnconfigure(1, weight=1)
        self.knowledgeFrame.grid_columnconfigure(2, weight=1)
        self.knowledgeFrame.grid_columnconfigure(3, weight=1)
        self.knowledgeFrame.grid_columnconfigure(4, weight=1)
        self.knowledgeFrame.grid_columnconfigure(5, weight=1)
        self.knowledgeFrame.grid_columnconfigure(6, weight=1)
        self.knowledgeFrame.grid_columnconfigure(7, weight=1)
        self.knowledgeFrame.grid(row=1, column=0, sticky="NSEW")

        knowledgeDict = self.controller.char.skill.knowledges
        knowledges = knowledgeDict.keys()
        knowledges.sort()

        self.populateFrame(self.knowledgeFrame, knowledgeDict, knowledges)

        self.bottomFrame = ttk.Frame(self.skillPage)
        self.bottomFrame.grid(row=2, column=0, sticky ="EW")

        tk.Label(self.bottomFrame, text="Skill Points: ").grid(row=0, column=0)
        tk.Label(self.bottomFrame, textvariable=self.controller.char.skillPoints.value).grid(row=0, column=1)


    def setSkillRank(self, rankValue, value):
        newValue = rankValue.get() + value
        skillPoints = self.controller.char.skillPoints

        if newValue >= 0 and newValue <= self.controller.char.charLevel.get() and skillPoints.value.get() - value >= 0:
            rankValue.set(newValue)
            skillPoints.baseValue.set(skillPoints.baseValue.get() - value)


    def populateFrame(self, parent, dict, list):
        i = 0
        for item in list:
            tk.Label(parent, text=item, font=("helvetica", 10)).grid(row=i, column=0, sticky="EW")
            tk.Label(parent, text=dict[item].statName, font=("helvetica", 10)).grid(row=i, column=1, sticky="EW")
            
            tk.Label(parent, text="Rank: ", font=("helvetica", 10)).grid(row=i, column=2, sticky="EW")

            rankValue = dict[item].rank

            # Rank Buttons
            self.rankButtons = ttk.Frame(parent)
            self.rankButtons.grid(row=i, column=3, sticky="W")
            commandUp = lambda rv=rankValue: self.setSkillRank(rv, 1)
            tk.Button(self.rankButtons, text="+", font=("helvetica", 6), command=commandUp).grid(row=0, column=0)
            
            tk.Label(parent, textvariable=rankValue, font=("helvetica", 10)).grid(row=i, column=4, sticky="EW")

            commandDown = lambda rv=rankValue: self.setSkillRank(rv, -1)
            tk.Button(self.rankButtons, text="-", font=("helvetica", 6), command=commandDown).grid(row=0, column=1)

            classSkill = tk.StringVar(value="Yes" if dict[item].classSkill.get() else "No")
            dict[item].classSkill.trace("w", lambda i,o,x, ds=dict[item].classSkill, cs=classSkill: cs.set("Yes" if ds.get() else "No"))

            tk.Label(parent, text="Total: ", font=("helvetica", 10)).grid(row=i, column=5, sticky="EW")
            tk.Label(parent, textvariable=dict[item].value, font=("helvetica", 10)).grid(row=i, column=6, sticky="EW")

            tk.Label(parent, textvariable=classSkill, font=("helvetica", 10)).grid(row=i, column=7, sticky="EW")

            i += 1
