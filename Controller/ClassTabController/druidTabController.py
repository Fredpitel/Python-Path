from View.ClassTab.druidTab import DruidTab 

class DruidTabController:
    def __init__(self, controller, parent):
        self.view = DruidTab(parent)


    def getView(self):
        return self.view.frame