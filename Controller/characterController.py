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

        self.skillPointRequirement = None


    def closeTab(self):
        self.parent.destroy(self.parent.select())


    def addClass(self, className, classData, nbLevels):
        if not className in self.char.charClass or self.char.charClass[className] is None:
            self.char.charClass[className] = CharClass(className, classData, nbLevels)
        else:
            self.char.charClass[className].nbLevels += nbLevels

        charClass = self.char.charClass[className]

        for skill in charClass.classSkills:
            if skill == "Perform":
                for perform in self.char.skill.performs:
                    if not self.char.skill.performs[perform].classSkill.get():
                        self.char.skill.performs[perform].classSkill.set(True)
            elif skill == "Craft":
                for craft in self.char.skill.crafts:
                    if not self.char.skill.crafts[craft].classSkill.get():
                        self.char.skill.crafts[craft].classSkill.set(True)
            elif skill == "Profession":
                for profession in self.char.skill.professions:
                    if not self.char.skill.professions[profession].classSkill.get():
                        self.char.skill.professions[profession].classSkill.set(True)
            else:
                charSkill = self.char.skill[skill]
                
                if not charSkill.classSkill.get():
                    charSkill.classSkill.set(True)

        self.calculateSpFromLevels()

        if self.skillPointRequirement is None:
            self.skillPointRequirement = self.addRequirement([self.char.skillPoints.value],
                                                             lambda: self.checkSkillPoints(),
                                                             "Skill Points remain to be spent",
                                                             [])


    def removeClass(self, className):
        charClass = self.char.charClass[className]
        charClass.nbLevels -= 1
        
        if charClass.nbLevels == 0:
            for skill in charClass.classSkills:
                if skill == "Perform":
                    for perform in self.char.skill.performs:
                        self.char.skill.performs[perform].classSkill.set(False)
                elif skill == "Craft":
                    for craft in self.char.skill.crafts:
                        self.char.skill.crafts[craft].classSkill.set(False)
                elif skill == "Profession":
                    for profession in self.char.skill.professions:
                        self.char.skill.professions[profession].classSkill.set(False)
                else:
                    self.char.skill[skill].classSkill.set(False)

            del self.char.charClass[className]

        self.calculateSpFromLevels()


    def calculateSpFromLevels(self):
        sp = 0
        
        charClasses = self.char.charClass

        for className in charClasses.keys():
            sp += charClasses[className].skillLevel * charClasses[className].nbLevels

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


