from tkinter     import *

class Skill:
    def __init__(self, value, untrained, penalty, stat):
        self.value     = IntVar(value=value)
        self.untrained = untrained
        self.penalty   = penalty
        self.stat      = stat
