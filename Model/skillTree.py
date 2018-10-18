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
            self.skills[skill] = Skill(self.skills_data["skills"][skill], self.controller)

        for knowledge in self.skills_data["knowledges"]:
            self.knowledges[knowledge] = Skill(self.skills_data["knowledges"][knowledge], self.controller)

        for perform in self.skills_data["performs"]:
            self.performs[perform] = Skill(self.skills_data["performs"][perform], self.controller)

        for craft in self.skills_data["crafts"]:
            self.crafts[craft] = Skill(self.skills_data["crafts"][craft], self.controller)

        for profession in self.skills_data["professions"]:
            self.professions[profession] = Skill(self.skills_data["professions"][profession], self.controller)


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
