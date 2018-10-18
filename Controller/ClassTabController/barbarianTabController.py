from View.ClassTab.barbarianTab import BarbarianTab 

class BarbarianTabController:
    def __init__(self, parent):
        self.view = BarbarianTab(parent)


    def getView(self):
        return self.view.frame