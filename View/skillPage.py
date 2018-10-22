#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

class SkillPage:
    def __init__(self, controller, parent):
        self.controller = controller
        
        self.bgStyle = ttk.Style()
        self.bgStyle.configure('White.TFrame', background="white")

        self.skillPage  = ttk.Frame(parent, relief=tk.RIDGE, padding=10)
        self.skillPage.grid(row=0, column=0, sticky= "NSEW")
        self.skillPage.grid_columnconfigure(0, weight=1, uniform="x")
        self.skillPage.grid_columnconfigure(1, weight=1, uniform="x")
        self.skillPage.grid_columnconfigure(2, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(0, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(1, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(2, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(3, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(4, weight=1, uniform="x")
        self.skillPage.grid_rowconfigure(5, weight=1, uniform="x")

        self.skillDict = self.controller.char.skill.skills
        
        #
        # Skill Frame
        #
        skills = []
        for skill in self.skillDict.keys():
            if self.skillDict[skill].list in ["Skill", "Knowledge"]:
                skills.append(skill)
        
        skills.sort()

        self.skillFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        tk.Label(self.skillFrame, text="SKILL", bg="white").grid(row=0, column=0, columnspan=5, sticky="EW")
        ttk.Separator(self.skillFrame).grid(row=1, column=0, columnspan=5, sticky="EW", pady=5)
        self.populateFrame(self.skillFrame, skills)
        self.skillFrame.grid(row=0, column=0, sticky="NSEW", rowspan=6)

        #
        # Perform Frame
        #
        self.performFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        self.performFrame.grid_rowconfigure(4, weight=1)
        self.performFrame.grid_propagate(0)

        tk.Label(self.performFrame, text="PERFORM", bg="white").grid(row=0,column=0, columnspan=5, sticky="EW")
        ttk.Separator(self.performFrame).grid(row=1, column=0, columnspan=5, sticky="EW", pady=5)
        innerFrame = self.populateFrame(self.performFrame)
        ttk.Separator(self.performFrame).grid(row=4, column=0, columnspan=5, sticky="SEW", pady=5)
        tk.Button(self.performFrame, text="Add", command= lambda i=innerFrame: self.controller.createSkillWindow("Perform", i)).grid(row=5, column=0, columnspan=5, sticky="SEW")

        self.performFrame.grid(row=0, column=1, sticky="NSEW", rowspan=2)

        #
        # Craft Frame
        #
        self.craftFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        self.craftFrame.grid_rowconfigure(4, weight=1)

        tk.Label(self.craftFrame, text="CRAFT", bg="white").grid(row=0,column=0, columnspan=5, sticky="EW")
        ttk.Separator(self.craftFrame).grid(row=1, column=0, columnspan=5, sticky="EW", pady=5)
        innerFrame = self.populateFrame(self.craftFrame)
        ttk.Separator(self.craftFrame).grid(row=4, column=0, columnspan=5, sticky="SEW", pady=5)
        tk.Button(self.craftFrame, text="Add", command= lambda i=innerFrame: self.controller.createSkillWindow("Craft", i)).grid(row=5, column=0, columnspan=5, sticky="SEW")

        self.craftFrame.grid(row=2, column=1, sticky="NSEW", rowspan=2)

        #
        # Profession Frame
        #
        self.professionFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        self.professionFrame.grid_rowconfigure(4, weight=1)

        tk.Label(self.professionFrame, text="PROFESSION", bg="white").grid(row=0,column=0, columnspan=5, sticky="EW")
        ttk.Separator(self.professionFrame).grid(row=1, column=0, columnspan=5, sticky="EW", pady=5)
        innerFrame = self.populateFrame(self.professionFrame)
        ttk.Separator(self.professionFrame).grid(row=4, column=0, columnspan=5, sticky="SEW", pady=5)
        tk.Button(self.professionFrame, text="Add", command= lambda i=innerFrame: self.controller.createSkillWindow("Profession", i)).grid(row=5, column=0, columnspan=5, sticky="SEW")

        self.professionFrame.grid(row=4, column=1, sticky="NSEW", rowspan=2)

        #
        # Summary Frame
        #
        self.summaryFrame = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        self.summaryFrame.grid(row=0, column=2, sticky="NSEW", rowspan=5)
        self.summaryFrame.grid_columnconfigure(0, weight=1)

        allSkills = self.skillDict.keys()
        allSkills.sort()

        self.skillFramesDict = {}

        i = 0
        for skillName in allSkills:
            skill = self.skillDict[skillName]

            frame = ttk.Frame(self.summaryFrame, style="White.TFrame")
            frame.grid_columnconfigure(0, weight=2, uniform="x")
            frame.grid_columnconfigure(1, weight=1, uniform="x")
            frame.grid_columnconfigure(2, weight=1, uniform="x")
            frame.grid_columnconfigure(3, weight=1, uniform="x")
            frame.grid_columnconfigure(4, weight=1, uniform="x")
            frame.grid_columnconfigure(5, weight=1, uniform="x")

            tk.Label(frame, text=skillName, font=("helvetica", 10), bg="white", anchor="w").grid(row=0, column=0, sticky="EW")
            tk.Label(frame, text=skill.statName, font=("helvetica", 10), bg="white").grid(row=0, column=1, sticky="EW")
            tk.Label(frame, textvariable=skill.value, font=("helvetica", 10), bg="white").grid(row=0, column=2, sticky="EW")
            tk.Label(frame, textvariable=skill.bonus, font=("helvetica", 10), bg="white").grid(row=0, column=3, sticky="EW")
            tk.Label(frame, textvariable=skill.rank, font=("helvetica", 10), bg="white").grid(row=0, column=4, sticky="EW")
            tk.Label(frame, textvariable=skill.modValue, font=("helvetica", 10), bg="white").grid(row=0, column=5, sticky="EW")

            frame.grid(row=i, column=0, sticky="EW")
            self.skillFramesDict[skill] = frame

            skill.rank.trace("w", lambda i,o,x: self.updateSkillSummary())
            skill.show.trace("w", lambda i,o,x: self.updateSkillSummary())
            i += 1

        self.updateSkillSummary()

        
        #
        # Skill Points Frame
        #
        self.skillPoints = ttk.Frame(self.skillPage, relief=tk.SUNKEN, padding=10, style="White.TFrame")
        self.skillPoints.grid(row=5, column=2, sticky ="NSEW")
        self.skillPoints.grid_columnconfigure(0, weight=1)
        self.skillPoints.grid_columnconfigure(1, weight=1)
        self.skillPoints.grid_rowconfigure(0, weight=1)

        tk.Label(self.skillPoints, text="Skill Points: ", font=("helvetica", 16), bg="white").grid(row=0, column=0, sticky="NSE")
        tk.Label(self.skillPoints, textvariable=self.controller.char.skillPoints.value, font=("helvetica", 16), bg="white").grid(row=0, column=1,sticky="NSW")

        self.skillPage.update_idletasks()


    def populateFrame(self, frame, list=[]):
        innerFrame = ttk.Frame(frame, style="White.TFrame")
        innerFrame.grid_columnconfigure(0, weight=1)

        header = ttk.Frame(innerFrame, style="White.TFrame")
        header.grid_columnconfigure(0, weight=2, uniform="x")
        header.grid_columnconfigure(1, weight=1, uniform="x")
        header.grid_columnconfigure(2, weight=1, uniform="x")
        header.grid_columnconfigure(3, weight=1, uniform="x")
        header.grid_columnconfigure(4, weight=1, uniform="x")

        tk.Label(header, text="Skill", font=("helvetica", 10), bg="white").grid(row=0, column=0, sticky="EW")
        tk.Label(header, text="Rank", font=("helvetica", 10), bg="white", anchor="w").grid(row=0, column=2, sticky="EW")
        tk.Label(header, text="Total", font=("helvetica", 10), bg="white").grid(row=0, column=3, sticky="EW")
        tk.Label(header, text="Class skill", font=("helvetica", 10), bg="white").grid(row=0, column=4, sticky="EW")
        
        header.pack(expand=True, fill="both")

        for skill in list:
            self.createSkillFrame(innerFrame, skill)

        innerFrame.grid(row=3, column=0, columnspan=5, sticky="NEWS")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_columnconfigure(4, weight=1)

        return innerFrame


    def createSkillFrame(self, parent, skill):
        frame = ttk.Frame(parent, style="White.TFrame")
        frame.grid_columnconfigure(0, weight=2, uniform="x")
        frame.grid_columnconfigure(1, weight=1, uniform="x")
        frame.grid_columnconfigure(2, weight=1, uniform="x")
        frame.grid_columnconfigure(3, weight=1, uniform="x")
        frame.grid_columnconfigure(4, weight=1, uniform="x")

        tk.Label(frame, text=skill + " (" + self.skillDict[skill].statName + ")", font=("helvetica", 10), anchor="w", bg="white").grid(row=0, column=0, sticky="EW")

        rankValue = self.skillDict[skill].rank

        tk.Label(frame, textvariable=rankValue, font=("helvetica", 10), anchor="w", bg="white").grid(row=0, column=1, sticky="E", padx=5)
        
        # Rank Buttons
        self.rankButtons = ttk.Frame(frame, style="White.TFrame")
        self.rankButtons.grid(row=0, column=2, sticky="W")

        commandUp = lambda rv=rankValue: self.controller.setSkillRank(rv, 1)
        tk.Button(self.rankButtons, text="▲", font=("helvetica", 8), borderwidth=1, highlightthickness=0, command=commandUp).grid(row=0, column=0)
        commandDown = lambda rv=rankValue: self.controller.setSkillRank(rv, -1)
        tk.Button(self.rankButtons, text="▼", font=("helvetica", 8), borderwidth=1, highlightthickness=0, command=commandDown).grid(row=0, column=1)

        classSkill = tk.StringVar(value="Yes" if self.skillDict[skill].classSkill.get() else "No")
        self.skillDict[skill].classSkill.trace("w", lambda i,o,x, ds=self.skillDict[skill].classSkill, cs=classSkill: cs.set("Yes" if ds.get() else "No"))

        tk.Label(frame, textvariable=self.skillDict[skill].value, font=("helvetica", 10), bg="white").grid(row=0, column=3, sticky="EW")

        tk.Label(frame, textvariable=classSkill, font=("helvetica", 10), bg="white").grid(row=0, column=4, sticky="EW")

        frame.pack(expand=True, fill="both")


    def updateSkillSummary(self):
        for skill in self.skillFramesDict:
            self.skillFramesDict[skill].grid_remove()

            if (skill.show.get() and skill.untrained) or skill.rank.get() > 0:
                self.skillFramesDict[skill].grid(sticky="EW")