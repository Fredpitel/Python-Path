from Controller.ClassTabController import *

class ClassTabControllerFactory:
    def __init__(self):
        self.classTabDict = {
            "Barbarian" : lambda c,p: BarbarianTabController(c,p),
            "Bard"      : lambda c,p: BardTabController(c,p),
            "Cleric"    : lambda c,p: ClericTabController(c,p),
            "Druid"     : lambda c,p: DruidTabController(c,p),
            "Fighter"   : lambda c,p: FighterTabController(c,p),
            "Monk"      : lambda c,p: MonkTabController(c,p),
            "Paladin"   : lambda c,p: PaladinTabController(c,p),
            "Ranger"    : lambda c,p: RangerTabController(c,p),
            "Rogue"     : lambda c,p: RogueTabController(c,p),
            "Sorcerer"  : lambda c,p: SorcererTabController(c,p),
            "Wizard"    : lambda c,p: WizardTabController(c,p)
        }


    def getController(self, controller, parent, className):
        return self.classTabDict[className](controller, parent)