from View.skillPage   import SkillPage
from View.skillWindow import SkillWindow

class SkillPageController:
    def __init__(self, controller):
        self.controller = controller
        self.char       = controller.char

        self.view = SkillPage(self, controller.nb)


    def getView(self):
        return self.view.skillPage


    def setSkillRank(self, rankValue, value):
        newValue = rankValue.get() + value
        skillPoints = self.controller.char.skillPoints


        if newValue >= 0 and newValue <= self.controller.char.charLevel.get():
            if (skillPoints.value.get() >= 0 and skillPoints.value.get() - value >= 0) or (skillPoints.value.get() < 0 and value < 0 ):
                rankValue.set(newValue)
                skillPoints.baseValue.set(skillPoints.baseValue.get() - value)
                self.controller.char.spentSP += value


    def createSkillWindow(self, list, frame):
        skillDict = self.controller.char.skill.skills
        skills = []

        for skill in skillDict:
            if skillDict[skill].list == list:
                skills.append(skill)

        SkillWindow(self, skills, frame)


    def addSkill(self, window, checkboxes, frame):
        window.destroy()

        for checkbox in checkboxes:
            if checkbox.var.get():
                self.view.createSkillFrame(frame, checkbox.skill)