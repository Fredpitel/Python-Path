from modifiable import Modifiable

class HP(Modifiable):
	def __init__(self, char, baseValue):
		Modifiable.__init__(self, baseValue)

		self.char = char
		self.char.con.bonus.trace(     "w", lambda i,o,x: self.update())
		self.char.hpFromLevels.trace(  "w", lambda i,o,x: self.update())


	def update(self):
		baseHP = self.char.charLevel.get() * self.char.con.bonus.get()
		baseHP += self.char.hpFromLevels.get()

		self.baseValue.set(baseHP)
		Modifiable.update(self)