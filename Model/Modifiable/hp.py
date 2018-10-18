from modifiable import Modifiable

class HP(Modifiable):
	def __init__(self, baseValue, char):
		Modifiable.__init__(self, baseValue)

		self.char = char
		self.char.con.bonus.trace(     "w", lambda i,o,x: self.updateBaseValue())
		self.char.hpFromLevels.trace(  "w", lambda i,o,x: self.updateBaseValue())


	def updateBaseValue(self):
		baseHP = self.char.charLevel.get() * self.char.con.bonus.get()
		baseHP += self.char.hpFromLevels.get()

		self.baseValue.set(baseHP)