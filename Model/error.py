import Tkinter as tk

class Error:
    def __init__(self, message):
        self.message   = tk.StringVar(value=message)
        self.label     = None


    def setMessage(self, message):
        self.message.set(message)