from View.ClassTab.bardTab import BardTab 

class BardTabController:
    def __init__(self, parent):
        self.view = BardTab(parent)


    def getView(self):
        return self.view.frame