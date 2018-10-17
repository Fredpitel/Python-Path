import json
import os

from Modifiable import Skill

class SkillTree:
    def __init__(self, controller):
        self.controller = controller
        
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
