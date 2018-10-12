import Tkinter as tk

class CharClass:
    def __init__(self, className, classData, nbLevels):
        self.className   = className
        self.skillLevel  = classData["skillLevel"]
        self.classSkills = classData["classSkills"]
        self.nbLevels    = nbLevels