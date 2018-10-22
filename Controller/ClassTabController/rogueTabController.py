from View.ClassTab.rogueTab import RogueTab 

class RogueTabController:
    def __init__(self, controller, parent):
        self.view = RogueTab(parent)


    def getView(self):
        return self.view.frame