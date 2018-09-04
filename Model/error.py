import Tkinter as tk

class Error:
    def __init__(self, message, problem, callback):
        self.message   = tk.StringVar(value=message)
        self.callback  = callback
        self.problem   = problem
        self.label     = None
        self.solutions = []


    def setMessage(self, message):
        self.message.set(message)


    def __eq__(self, other):
        return self.message.get() == other.message.get() and self.problem == other.problem


    def __ne__(self, other):
        return self.message.get() != other.message.get() or self.problem != other.problem


class Solution:
    def __init__(self, solution, traceId):
        self.solution = solution
        self.traceId  = traceId