from modifiable import *

class Skill(Modifiable):
    def __init__(self, char, baseValue, untrained, penalty, stat):
        Modifiable.__init__(self, char, baseValue)
        self.untrained  = untrained
        self.penalty    = penalty
        self.stat       = stat
        self.classSkill = False