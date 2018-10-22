from View.ClassTab.fighterTab import FighterTab 

class FighterTabController:
    def __init__(self, controller, parent):
        self.view = FighterTab(parent)


    def getView(self):
        return self.view.frame