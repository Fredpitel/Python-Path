from tkinter import *
from decimal import *

class Modifiable:
	def __init__(self, char, baseValue):
		self.char      = char
		self.baseValue = IntVar(value=baseValue)
		self.value     = IntVar(value=baseValue)
		self.modValue  = IntVar(value=0)


	def update(self):
		self.modValue.set(self.getModValue())
		self.value.set(self.baseValue.get() + self.modValue.get())


	def getModValue(self):
		total = 0
		for type in self.char.modifiers[self].keys():
			if type in self.char.STACKABLE_TYPES:
				for source in self.char.modifiers[self][type].keys():
					total += self.char.modifiers[self][type][source]
			else:
				maxMod = {"source": "", "value": Decimal('-Infinity')}
				for source in self.char.modifiers[self][type].keys():
					if self.char.modifiers[self][type][source] > maxMod["value"] and source != maxMod["source"]:
						maxMod = {"source": source, "value": self.char.modifiers[self][type][source]}

				total += maxMod["value"]

		return total