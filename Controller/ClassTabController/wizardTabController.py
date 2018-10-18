from View.ClassTab.wizardTab import WizardTab 

class WizardTabController:
    def __init__(self, parent):
        self.view = WizardTab(parent)


    def getView(self):
        return self.view.frame