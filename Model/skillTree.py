from Modifiable import Skill

class SkillTree:
    def __init__(self, controller):
        self.controller = controller

        self.skills = {
            "Acrobatics"                : Skill(0, True,  True,  "dex", self.controller),
            "Appraise"                  : Skill(0, True,  False, "int", self.controller),
            "Bluff"                     : Skill(0, True,  False, "cha", self.controller),
            "Climb"                     : Skill(0, True,  True,  "str", self.controller),
            "Diplomacy"                 : Skill(0, True,  False, "cha", self.controller),
            "Disable Device"            : Skill(0, False, True,  "dex", self.controller),
            "Disguise"                  : Skill(0, True,  False, "cha", self.controller),
            "Escape Artist"             : Skill(0, True,  True,  "dex", self.controller),
            "Fly"                       : Skill(0, True,  True,  "dex", self.controller),
            "Handle Animal"             : Skill(0, False, False, "cha", self.controller),
            "Heal"                      : Skill(0, True,  False, "wis", self.controller),
            "Intimidate"                : Skill(0, True,  False, "cha", self.controller),
            "Linguistics"               : Skill(0, False, False, "int", self.controller),
            "Perception"                : Skill(0, True,  False, "wis", self.controller),
            "Ride"                      : Skill(0, True,  True,  "dex", self.controller),
            "Sense Motive"              : Skill(0, True,  False, "wis", self.controller),
            "Sleight of Hand"           : Skill(0, False, True,  "dex", self.controller),
            "Spellcraft"                : Skill(0, False, False, "int", self.controller),
            "Stealth"                   : Skill(0, True,  True,  "dex", self.controller),
            "Survival"                  : Skill(0, True,  False, "wis", self.controller),
            "Swim"                      : Skill(0, True,  True,  "str", self.controller),
            "Use Magic Device"          : Skill(0, False, False, "cha", self.controller)
        }

        self.knowledges = {
            "Knowledge (arcana)"        : Skill(0, False, False, "int", self.controller),
            "Knowledge (dungeoneering)" : Skill(0, False, False, "int", self.controller),
            "Knowledge (engineering)"   : Skill(0, False, False, "int", self.controller),
            "Knowledge (geography)"     : Skill(0, False, False, "int", self.controller),
            "Knowledge (history)"       : Skill(0, False, False, "int", self.controller),
            "Knowledge (local)"         : Skill(0, False, False, "int", self.controller),
            "Knowledge (nature)"        : Skill(0, False, False, "int", self.controller),
            "Knowledge (nobility)"      : Skill(0, False, False, "int", self.controller),
            "Knowledge (planes)"        : Skill(0, False, False, "int", self.controller),
            "Knowledge (religion)"      : Skill(0, False, False, "int", self.controller),
        }

        self.performs = {
            "Perform (act)"             : Skill(0, True,  False, "cha", self.controller),
            "Perform (comedy)"          : Skill(0, True,  False, "cha", self.controller),
            "Perform (dance)"           : Skill(0, True,  False, "cha", self.controller),
            "Perform (keyboard)"        : Skill(0, True,  False, "cha", self.controller),
            "Perform (oratory)"         : Skill(0, True,  False, "cha", self.controller),
            "Perform (percussion)"      : Skill(0, True,  False, "cha", self.controller),
            "Perform (string)"          : Skill(0, True,  False, "cha", self.controller),
            "Perform (wind)"            : Skill(0, True,  False, "cha", self.controller),
            "Perform (sing)"            : Skill(0, True,  False, "cha", self.controller),
        }

        self.crafts = {
            "Craft"                     : Skill(0, True,  False, "int", self.controller), #TODO
        }

        self.professions = {
            "Profession"                : Skill(0, False, False, "wis", self.controller), #TODO
        }


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
