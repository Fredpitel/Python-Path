import ttk
import Tkinter as tk

class ErrorFrame():
	def __init__(self, controller, parent):
		self.errorFrame = ttk.Frame(parent, relief=tk.SUNKEN, padding=10)
		self.errorFrame.grid(row=1, column=0, padx=10, sticky="SEW")
		self.errorFrame.grid_propagate(0)


	def addLabel(self, message):
		label = tk.Label(self.errorFrame, textvariable=message, font=('Helvetica', 12), fg="red")
		label.pack(expand=True)

		return label