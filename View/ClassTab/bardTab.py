import ttk
import Tkinter as tk

from classTab import ClassTab

class BardTab(ClassTab):
    def __init__(self, parent):
        self.parent = parent
        
        ClassTab.__init__(self, self.parent)