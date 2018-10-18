import json
import os

from Modifiable import Skill

class SkillTree:
    def __init__(self, controller):
        self.controller = controller
        self.char       = controller.char

        self.skills      = {}
        self.knowledges  = {}
        self.performs    = {}
        self.crafts      = {}
        self.professions = {}
        
        self.skills_data = json.load(open(os.path.abspath("Data/skills.json")))
        
        for skill in self.skills_data["skills"]:
            data = self.skills_data["skills"][skill]
            self.skills[skill] = Skill(0, data["untrained"], data["penalty"], data["stat"], self.controller)

        for knowledge in self.skills_data["knowledges"]:
            data = self.skills_data["knowledges"][knowledge]
            self.knowledges[knowledge] = Skill(0, data["untrained"], data["penalty"], data["stat"], self.controller)

        for perform in self.skills_data["performs"]:
            data = self.skills_data["performs"][perform]
            self.performs[perform] = Skill(0, data["untrained"], data["penalty"], data["stat"], self.controller)

        for craft in self.skills_data["crafts"]:
            data = self.skills_data["crafts"][craft]
            self.crafts[craft] = Skill(0, data["untrained"], data["penalty"], data["stat"], self.controller)

        for profession in self.skills_data["professions"]:
            data = self.skills_data["professions"][profession]
            self.professions[profession] = Skill(0, data["untrained"], data["penalty"], data["stat"], self.controller)


    def setClassSkill(self, classSkills, value):
        for skill in classSkills:
            if skill == "Knowledge":
                for knowledge in self.knowledges:
                    if not self.knowledges[knowledge].classSkill.get():
                        self.knowledges[knowledge].classSkill.set(value)
            elif skill == "Perform":
                for perform in self.performs:
                    if not self.performs[perform].classSkill.get():
                        self.performs[perform].classSkill.set(value)
            elif skill == "Craft":
                for craft in self.crafts:
                    if not self.crafts[craft].classSkill.get():
                        self.crafts[craft].classSkill.set(value)
            elif skill == "Profession":
                for profession in self.professions:
                    if not self.professions[profession].classSkill.get():
                        self.professions[profession].classSkill.set(value)
            else:
                if not self.__getitem__(skill).classSkill.get():
                    self.__getitem__(skill).classSkill.set(value)


    def __getitem__(self, skill):
        try :
            return self.skills[skill]
        except:
            try:
                return self.knowledges[skill]
            except:
                try:
                    return self.performs[skill]
                except:
                    try:
                        return self.crafts[skill]
                    except:
                        return self.professions[skill]
