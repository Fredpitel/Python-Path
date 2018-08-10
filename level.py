from tkinter  import *

class Level:
    def __init__(self, charClass, hpGained):
        self.charClass = charClass
        self.hpGained = IntVar(value=hpGained)