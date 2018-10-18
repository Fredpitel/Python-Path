from Controller.ClassTabController import *

class ClassTabControllerFactory:
    def __init__(self):
        self.classTabDict = {
            "Barbarian" : lambda p: BarbarianTabController(p),
            "Bard"      : lambda p: BardTabController(p),
            "Cleric"    : lambda p: ClericTabController(p),
            "Druid"     : lambda p: DruidTabController(p),
            "Fighter"   : lambda p: FighterTabController(p),
            "Monk"      : lambda p: MonkTabController(p),
            "Paladin"   : lambda p: PaladinTabController(p),
            "Ranger"    : lambda p: RangerTabController(p),
            "Rogue"     : lambda p: RogueTabController(p),
            "Sorcerer"  : lambda p: SorcererTabController(p),
            "Wizard"    : lambda p: WizardTabController(p)
        }


    def getController(self, parent, className):
        return self.classTabDict[className](parent)