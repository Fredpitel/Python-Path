from View.ClassTab.monkTab import MonkTab 

class MonkTabController:
    def __init__(self, parent):
        self.view = MonkTab(parent)


    def getView(self):
        return self.view.frame