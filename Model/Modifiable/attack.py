from modifiable import Modifiable

class Attack(Modifiable):
    def __init__(self, char, baseValue):
        Modifiable.__init__(self, char, baseValue)