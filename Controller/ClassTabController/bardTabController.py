import Tkinter as tk

from View.ClassTab.bardTab import BardTab 

class BardTabController:
    def __init__(self, controller, parent):
        self.parent     = parent
        self.controller = controller
        
        self.view = BardTab(self.parent)
        self.knowledgeBonus = tk.IntVar(value=max(1, int(self.controller.char.charClass["Bard"].nbLevels / 2)))

        skillDict = self.controller.char.skill.skills
        for skill in skillDict:
            if skillDict[skill].list == "Knowledge":
                skillDict[skill].untrained = True
                skillDict[skill].show.set(True)
                skillDict[skill].addModifier({"target" : skillDict[skill],
                                              "type"   : "untyped",
                                              "value"  : self.knowledgeBonus.get()},
                                              self.knowledgeBonus)

        self.controller.char.charLevel.trace("w", lambda i,o,x: self.updateKnowledgeBonus())


    def getView(self):
        return self.view.frame


    def updateKnowledgeBonus(self):
        self.knowledgeBonus.set(min(1, int(self.controller.char.charClass["Bard"].nbLevels / 2)))
        skillDict = self.controller.char.skill.skills
        for skill in skillDict:
            if skillDict[skill].list == "Knowledge":
                skillDict[skill].addModifier({"target" : skillDict[skill],
                                              "type"   : "untyped",
                                              "value"  : self.knowledgeBonus.get()},
                                              self.knowledgeBonus)