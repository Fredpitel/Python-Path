from View.ClassTab.rangerTab import RangerTab 

class RangerTabController:
    def __init__(self, parent):
        self.view = RangerTab(parent)


    def getView(self):
        return self.view.frame