from View.ClassTab.clericTab import ClericTab 

class ClericTabController:
    def __init__(self, controller, parent):
        self.view = ClericTab(parent)


    def getView(self):
        return self.view.frame