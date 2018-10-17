#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

class SkillPage:
    def __init__(self, controller, parent):
        self.controller = controller

        self.skillPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.skillPage.grid(row=0, column=0, sticky= "NSEW")
        self.skillPage.grid_columnconfigure(0, weight=1)
        self.skillPage.grid_columnconfigure(1, weight=1)
        self.skillPage.grid_columnconfigure(2, weight=1)


        skillDict = self.controller.char.skill.skills
        skills = skillDict.keys()
        skills.sort()

        self.skillFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        tk.Label(self.skillFrame, text="SKILL").grid(row=0,column=0, columnspan=8, sticky="EW")
        self.populateFrame(self.skillFrame, skillDict, skills)
        self.skillFrame.grid(row=0, column=0, sticky="NSEW", rowspan=3)

        knowledgeDict = self.controller.char.skill.knowledges
        knowledges = knowledgeDict.keys()
        knowledges.sort()

        self.knowledgeFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        tk.Label(self.knowledgeFrame, text="KNOWLEDGE").grid(row=0,column=0, columnspan=8, sticky="EW")
        self.populateFrame(self.knowledgeFrame, knowledgeDict, knowledges)
        self.knowledgeFrame.grid(row=3, column=0, sticky="NSEW", rowspan=2)

        performDict = self.controller.char.skill.performs
        performs = performDict.keys()
        performs.sort()

        self.performFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        tk.Label(self.performFrame, text="PERFORM").grid(row=0,column=0, columnspan=8, sticky="EW")
        self.populateFrame(self.performFrame, performDict, performs)
        self.performFrame.grid(row=0, column=1, sticky="NSEW", rowspan=2)

        craftDict = self.controller.char.skill.crafts
        crafts = craftDict.keys()
        crafts.sort()

        self.craftFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        tk.Label(self.craftFrame, text="CRAFT").grid(row=0,column=0, columnspan=8, sticky="EW")
        self.populateFrame(self.craftFrame, craftDict, crafts)
        self.craftFrame.grid(row=2, column=1, sticky="NSEW", rowspan=3)

        professionDict = self.controller.char.skill.professions
        professions = professionDict.keys()
        professions.sort()

        self.professionFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        tk.Label(self.professionFrame, text="PROFESSION").grid(row=0,column=0, columnspan=8, sticky="EW")
        self.populateFrame(self.professionFrame, professionDict, professions)
        self.professionFrame.grid(row=0, column=2, sticky="NSEW", rowspan=4)

        self.bottomFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10)
        self.bottomFrame.grid(row=4, column=2, sticky ="NSEW")
        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_columnconfigure(1, weight=1)
        self.bottomFrame.grid_rowconfigure(0, weight=1)

        tk.Label(self.bottomFrame, text="Skill Points: ", font=("helvetica", 16)).grid(row=0, column=0, sticky="NSE")
        tk.Label(self.bottomFrame, textvariable=self.controller.char.skillPoints.value, font=("helvetica", 16)).grid(row=0, column=1,sticky="NSW")

        self.skillPage.update_idletasks()


    def populateFrame(self, frame, dict, list):
        tk.Label(frame, text="Skill", font=("helvetica", 10)).grid(row=1, column=0, sticky="EW")
        tk.Label(frame, text="Rank", font=("helvetica", 10), anchor="w").grid(row=1, column=1, sticky="EW", columnspan=2)
        tk.Label(frame, text="Total", font=("helvetica", 10)).grid(row=1, column=3, sticky="EW")
        tk.Label(frame, text="Class skill", font=("helvetica", 10)).grid(row=1, column=4, sticky="EW")
        
        i = 2
        for item in list:
            tk.Label(frame, text=item + " (" + dict[item].statName + ")", font=("helvetica", 10), anchor="w").grid(row=i, column=0, sticky="EW")

            rankValue = dict[item].rank

            tk.Label(frame, textvariable=rankValue, font=("helvetica", 10), anchor="w").grid(row=i, column=1, sticky="EW")
            
            # Rank Buttons
            self.rankButtons = ttk.Frame(frame)
            self.rankButtons.grid(row=i, column=2, sticky="W")

            commandUp = lambda rv=rankValue: self.controller.setSkillRank(rv, 1)
            tk.Button(self.rankButtons, text="▲", font=("helvetica", 6), command=commandUp).grid(row=0, column=0)
            commandDown = lambda rv=rankValue: self.controller.setSkillRank(rv, -1)
            tk.Button(self.rankButtons, text="▼", font=("helvetica", 6), command=commandDown).grid(row=0, column=1)

            classSkill = tk.StringVar(value="Yes" if dict[item].classSkill.get() else "No")
            dict[item].classSkill.trace("w", lambda i,o,x, ds=dict[item].classSkill, cs=classSkill: cs.set("Yes" if ds.get() else "No"))

            tk.Label(frame, textvariable=dict[item].value, font=("helvetica", 10)).grid(row=i, column=3, sticky="EW")

            tk.Label(frame, textvariable=classSkill, font=("helvetica", 10)).grid(row=i, column=4, sticky="EW")

            i += 1

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_columnconfigure(4, weight=1)
