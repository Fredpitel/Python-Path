from View.ClassTab.sorcererTab import SorcererTab 

class SorcererTabController:
    def __init__(self, parent):
        self.view = SorcererTab(parent)


    def getView(self):
        return self.view.frame