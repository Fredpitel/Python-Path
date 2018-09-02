import Tkinter as tk

class Error:
    def __init__(self, message, callback, problem):
        self.message   = tk.StringVar(value=message)
        self.callback  = callback
        self.problem   = problem
        self.label     = None
    	self.solutions = []


    def setMessage(self, message):
    	self.message.set(message)


class Solution:
	def __init__(self, solution, traceId):
		self.solution = solution
		self.traceId  = traceId