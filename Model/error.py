import Tkinter as tk

class Error:
    def __init__(self, message, problems):
        self.message   = tk.StringVar(value=message)
        self.problems  = problems
        self.label     = None


    def setMessage(self, message):
        self.message.set(message)