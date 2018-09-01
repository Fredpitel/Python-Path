import Tkinter as tk

class Error:
    def __init__(self, source, message, parent, problem):
        self.source  = source
        self.message = message
        self.label   = tk.Label(parent, text=message, font=('Helvetica', 12), fg="red")
        self.label.pack(expand=True)
        self.problem = problem

    