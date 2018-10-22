import json
import os

from Modifiable import Skill

class SkillTree:
    def __init__(self, controller):
        self.controller = controller
        self.char       = controller.char

        self.skills      = {}
        self.skills_data = json.load(open(os.path.abspath("Data/skills.json")))
        
        for list in ["Skill", "Knowledge", "Perform", "Craft", "Profession"]:
            for skill in self.skills_data[list]:
                self.skills[skill] = Skill(self.skills_data[list][skill], list, self.controller)


    def setClassSkill(self, classSkills, value):
        for classSkill in classSkills:
            if classSkill in ["Knowledge", "Perform", "Craft", "Profession"]:
                for skill in self.skills.keys():
                    if self.skills[skill].list == classSkill:
                        if not self.__getitem__(skill).classSkill.get():
                            self.__getitem__(skill).classSkill.set(value)
            else:
                if not self.__getitem__(classSkill).classSkill.get():
                    self.__getitem__(classSkill).classSkill.set(value)


    def __getitem__(self, skill):
        return self.skills[skill]

