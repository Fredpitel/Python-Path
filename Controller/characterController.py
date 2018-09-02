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
        self.nb.grid(row=1, column=0, sticky="NSWE")

        self.char = Character(self)

        self.creationPageController = CreationPageController(self)
        self.errorFrameController   = ErrorFrameController(self)
        #self.sheetPageControlller   = SheetPageController(self)
        
        self.nb.add(self.creationPageController.getView(), text='Character Creation')

        # Initial errors
        self.addError("Choose a race",
                      None,
                      [self.creationPageController.race],
                      self.creationPageController.view.racesMenu)
        self.addError("Buy points remain to be spent",
                      self.creationPageController.checkBuyPointsError,
                      [self.creationPageController.buyPoints, self.creationPageController.maxBuyPoints],
                      self.creationPageController.view.buyPointsLabel)
        self.addError("Choose a class",
                      None,
                      [self.creationPageController.charClass],
                      self.creationPageController.view.classMenu)


    def closeTab(self):
        self.parent.forget(self.parent.select())


    def addError(self, msg, callback, solutions, problem):
        self.errorFrameController.addError(msg, callback, solutions, problem)