import Tkinter as tk

class CharClass:
    def __init__(self, className, classData, nbLevels):
        self.className   = className
        self.nbLevels    = tk.IntVar(value=nbLevels)
        
        self.skillLevel  = classData["skillLevel"]
        self.classSkills = classData["classSkills"]
        self.attackProg  = classData["attackProg"]
        self.fortProg    = classData["fortProg"]
        self.refProg     = classData["refProg"]
        self.willProg    = classData["willProg"]