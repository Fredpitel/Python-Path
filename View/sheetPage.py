import ttk
from tkinter import *

class StatsPage:
    def __init__(self, nb, char):
        statsPage = ttk.Frame(nb, relief=RIDGE, padding=10)
        nb.add(statsPage, text='Character Sheet', padding=10)
        
        self.char = char

        # Name
        Label(statsPage, text="Character Name: ").grid(row=0, column=0)
        Label(statsPage, textvariable=self.char.charName).grid(row=0, column=1)