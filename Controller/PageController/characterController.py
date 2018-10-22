import ttk
import Tkinter as tk

from Controller.PageController                               import *
from Controller.ClassTabController.classTabControllerFactory import ClassTabControllerFactory

from Model.character               import Character
from Model.requirement             import Requirement
from Model.charClass               import CharClass
from View.characterFrame           import CharacterFrame
from math                          import floor

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
        
        self.classTabControllers = {}

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

        self.addRequirement([self.char.skillPoints.value],
                             lambda: self.checkSkillPoints(),
                             "Skill Points remain to be spent",
                             [])


    def closeTab(self):
        self.parent.forget(self.parent.select())


    def addClass(self, className, classData, nbLevels):
        if not className in self.char.charClass or self.char.charClass[className] is None:
            self.char.charClass[className] = CharClass(className, classData, nbLevels)
        else:
            self.char.charClass[className].nbLevels.set(self.char.charClass[className].nbLevels.get() + nbLevels)

        if not className in self.classTabControllers:
            self.classTabControllers[className] = ClassTabControllerFactory().getController(self, self.nb, className)
            self.nb.insert(1, self.classTabControllers[className].getView(), text=className)

        self.char.skill.setClassSkill(self.char.charClass[className].classSkills, True)
        self.calculateSpFromLevels()
        self.updateStats()


    def removeClass(self, className):
        charClass = self.char.charClass[className]
        charClass.nbLevels.set(self.char.charClass[className].nbLevels.get() - 1)
        
        if charClass.nbLevels.get() == 0:
            self.nb.forget(self.classTabControllers[className].getView())
            self.char.skill.setClassSkill(charClass.classSkills, False)

            del self.classTabControllers[className]
            del self.char.charClass[className]

        self.calculateSpFromLevels()
        self.updateStats()


    def calculateSpFromLevels(self):
        sp = 0
        
        charClasses = self.char.charClass

        for className in charClasses.keys():
            sp += charClasses[className].skillLevel * charClasses[className].nbLevels.get()

        sp -= self.char.spentSP

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


    def checkSkillPoints(self):
        if self.char.skillPoints.value.get() > 0:
            return (False, "Skill Points remain to be spent")
        elif self.char.skillPoints.value.get() < 0:
            return (False, "Too many skill points spent")
        else:
            return (True, None)


    def updateStats(self):
        self.char.attack.updateBaseValue()
        self.char.fortitude.updateBaseValue()
        self.char.reflex.updateBaseValue()
        self.char.will.updateBaseValue()

        bab = self.char.getBab()
        nbAttack = int(floor(bab / 6)) + 1
        attackString = ""

        for i in range(0, int(nbAttack)):
            babValue = "+" + str(bab) if bab > 0 else str(bab)
            attackString = attackString + str(babValue) + "/"
            bab -= 5

        self.char.babString.set(attackString[:-1])

