from View.skillPage import SkillPage

class SkillPageController:
    def __init__(self, controller):
        self.controller = controller
        self.char       = controller.char

        self.view = SkillPage(self, controller.nb)


    def getView(self):
        return self.view.skillPage