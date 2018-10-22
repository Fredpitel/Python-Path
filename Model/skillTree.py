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
                for skill in self.skills:
                    if self.skills[skill].list == classSkill:
                        self.__getitem__(skill).classSkill.set(value)
            else:
                self.__getitem__(classSkill).classSkill.set(value)


    def __getitem__(self, skill):
        return self.skills[skill]

