import ttk
import Tkinter as tk

from Controller          import *
from Model.character     import Character
from Model.requirement   import Requirement
from View.characterFrame import CharacterFrame
#from sheetPage           import SheetPage

class CharacterController:
    def __init__(self, parent):
        self.parent = parent
        self.view = CharacterFrame(self, parent).characterFrame
        
        self.nb = ttk.Notebook(self.view)
        self.nb.grid(row=0, column=0, sticky="NSWE")

        self.char = Character(self)

        self.creationPageController = CreationPageController(self)
        self.errorFrameController   = ErrorFrameController(self, self.creationPageController.getView())
        #self.sheetPageControlller   = SheetPageController(self)
        
        self.nb.add(self.creationPageController.getView(), text='Character Creation')

        # Initial requirements
        self.addRequirement([self.char.race],
                            lambda: (self.char.race.get() != "Choose race", None),
                            "Choose a race",
                            [self.creationPageController.view.racesMenu])
        self.addRequirement([self.creationPageController.buyPoints, self.creationPageController.maxBuyPoints],
                            lambda: self.creationPageController.checkBuyPointsError(),
                            "Buy points remain to be spent",
                            [self.creationPageController.view.buyPointsLabel])
        self.addRequirement([self.creationPageController.charClass],
                            lambda: (self.creationPageController.charClass.get() != "Choose class", None),
                            "Choose a class",
                            [self.creationPageController.view.classMenu])
        self.addRequirement([self.char.alignment],
                            lambda: (self.char.alignment.get() != "Choose alignment", None),
                            "Choose an alignment",
                            [self.creationPageController.view.alignmentMenu])


    def closeTab(self):
        self.parent.forget(self.parent.select())


    def addMod(self, mod, source, toggler=None):
        target = self.getTarget(mod["target"])
        target.addModifier(mod, source, toggler)


    def removeMod(self, source, targetName):
        target = self.getTarget(targetName)
        target.removeModifier(source)


    def addError(self, msg):
        return self.errorFrameController.addError(msg)


    def removeError(self, error):
        self.errorFrameController.removeError(error)


    def getTarget(self, targetName):
        try:
            return getattr(self.char, targetName)
        except AttributeError:
            skill = targetName.split('"')[1]
            return self.char.skill[skill]


    def addRequirement(self, targets, condition, message, problems):
        return Requirement(self, targets, condition, message, problems)