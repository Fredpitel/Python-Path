import ttk
import Tkinter as tk

from Controller          import *
from Model.character     import Character
from Model.requirement   import Requirement
from Model.charClass     import CharClass
from View.characterFrame import CharacterFrame

class CharacterController:
    def __init__(self, parent):
        self.parent = parent
        self.view = CharacterFrame(self, parent).characterFrame
        
        self.nb = ttk.Notebook(self.view)
        self.nb.grid(row=0, column=0, sticky="NSWE")

        self.char = Character(self)
        self.char.createSkillTree(self)

        self.creationPageController = CreationPageController(self)
        self.errorFrameController   = ErrorFrameController(self, self.creationPageController.getView())
        self.skillPageController    = SkillPageController(self)
        self.sheetPageControlller   = SheetPageController(self)
        
        self.nb.add(self.creationPageController.getView(), text="Character Creation")
        self.nb.add(self.skillPageController.getView(), text="Skills")
        self.nb.add(self.sheetPageControlller.getView(), text="Character Sheet")

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


    def addClass(self, className, classData, nbLevels):

        if not className in self.char.charClass or self.char.charClass[className] is None:
            self.char.charClass[className] = CharClass(className, classData, nbLevels)
            charClass = self.char.charClass[className]
        else:
            self.char.charClass[className].nbLevels += nbLevels

        for skill in charClass.classSkills:
            charSkill = self.char.skill[skill]
            
            if not charSkill.classSkill.get():
                charSkill.classSkill.set(True)

        self.calculateSpFromLevels()


    def removeClass(self, className):
        charClass = self.char.charClass[className]
        charClass.nbLevels -= 1
        
        if charClass.nbLevels == 0:
            for skill in charClass.classSkills:
                self.char.skill[skill].classSkill.set(False)

            del self.char.charClass[className]

        self.calculateSpFromLevels()


    def calculateSpFromLevels(self):
        sp = 0
        
        charClasses = self.char.charClass

        for className in charClasses.keys():
            sp += charClasses[className].skillLevel * charClasses[className].nbLevels

        self.char.spFromLevels.set(sp)


    def addMod(self, mod, source):
        target = self.getTarget(mod["target"])
        target.addModifier(mod, source)


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
        except AttributeError as e:
            skill = targetName.split('"')[1]
            return self.char.skill[skill]


    def addRequirement(self, targets, condition, message, problems):
        return Requirement(self, targets, condition, message, problems)


