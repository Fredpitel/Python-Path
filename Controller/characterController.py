import ttk
import Tkinter as tk

from Controller          import *
from Model.character     import Character
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
        self.errorFrameController   = ErrorFrameController(self)
        #self.sheetPageControlller   = SheetPageController(self)
        
        self.nb.add(self.creationPageController.getView(), text='Character Creation')

        # Initial errors
        self.addError("Choose a race",
                      [self.creationPageController.race],
                      self.creationPageController.view.racesMenu)
        self.addError("Buy points remain to be spent",
                      [self.creationPageController.buyPoints, self.creationPageController.maxBuyPoints],
                      self.creationPageController.view.buyPointsLabel,
                      self.creationPageController.checkBuyPointsError)
        self.addError("Choose a class",
                      [self.creationPageController.charClass],
                      self.creationPageController.view.classMenu)


    def closeTab(self):
        self.parent.forget(self.parent.select())


    def addMod(self, mod, source, toggler=None):
        target = self.getTarget(mod["target"])
        target.addModifier(mod, source, toggler)


    def getTarget(self, targetName):
        try:
            return getattr(self.char, targetName)
        except AttributeError:
            skill = targetName.split('"')[1]
            return self.char.skill[skill]


    def addError(self, msg, solutions, problem, callback=None):
        self.errorFrameController.addError(msg, solutions, problem, callback)


    def removeError(self, error):
        self.errorFrameController.removeError(error)


    def findErrorBySolution(self, solution):
        return self.errorFrameController.findErrorBySolution(solution)