from View.ClassTab.paladinTab import PaladinTab 

class PaladinTabController:
    def __init__(self, controller, parent):
        self.view = PaladinTab(parent)


    def getView(self):
        return self.view.frame