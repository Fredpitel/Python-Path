import Tkinter as tk

from View.ClassTab.bardTab import BardTab 

class BardTabController:
    def __init__(self, controller, parent):
        self.parent     = parent
        self.controller = controller
        
        self.view = BardTab(self.parent)
        self.knowledgeBonus = tk.IntVar()
        self.classLevel = self.controller.char.charClass["Bard"].nbLevels

        self.updateKnowledgeBonus()
        self.setKnowledgesUntrained(True)

        self.classLevel.trace("w", lambda i,o,x: self.updateKnowledgeBonus())


    def getView(self):
        return self.view.frame


    def updateKnowledgeBonus(self):
        if self.classLevel.get() > 0:
            self.knowledgeBonus.set(max(1, int(self.classLevel.get() / 2)))
            skillDict = self.controller.char.skill.skills
            for skill in skillDict:
                if skillDict[skill].list == "Knowledge":
                    skillDict[skill].addModifier({"target" : skillDict[skill],
                                                  "type"   : "untyped",
                                                  "value"  : self.knowledgeBonus.get()},
                                                  self.knowledgeBonus)
        else:
            self.knowledgeBonus.set(0)
            self.setKnowledgesUntrained(False)


    def setKnowledgesUntrained(self, value):
        skillDict = self.controller.char.skill.skills
        for skill in skillDict:
            if skillDict[skill].list == "Knowledge":
                skillDict[skill].untrained = value
                skillDict[skill].show.set(value)