from modifiable import Modifiable

class HP(Modifiable):
	def __init__(self, char, baseValue):
		Modifiable.__init__(self, char, baseValue)

		self.char.con.bonus.trace("w", lambda i,o,x: self.update())
		self.char.charLevel.trace("w", lambda i,o,x: self.update())


	def update(self):
		baseHP = self.char.charLevel.get() * self.char.con.bonus.get()

		for level in self.char.levels:
			baseHP += level.hpGained.get()

		self.baseValue.set(baseHP)
		Modifiable.update(self)