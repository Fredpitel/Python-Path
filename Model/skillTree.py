from Modifiable import Skill

class SkillTree:
    def __init__(self):
        self.tree = {
            "Acrobatics"                : Skill(0, True,  True,  "dex"),
            "Appraise"                  : Skill(0, True,  False, "int"),
            "Bluff"                     : Skill(0, True,  False, "cha"),
            "Climb"                     : Skill(0, True,  True,  "str"),
            "Craft"                     : Skill(0, True,  False, "int"), #TODO
            "Diplomacy"                 : Skill(0, True,  False, "cha"),
            "Disable Device"            : Skill(0, False, True,  "dex"),
            "Disguise"                  : Skill(0, True,  False, "cha"),
            "Escape Artist"             : Skill(0, True,  True,  "dex"),
            "Fly"                       : Skill(0, True,  True,  "dex"),
            "Handle Animal"             : Skill(0, False, False, "cha"),
            "Heal"                      : Skill(0, True,  False, "wis"),
            "Intimidate"                : Skill(0, True,  False, "cha"),
            "Knowledge (arcana)"        : Skill(0, False, False, "int"),
            "Knowledge (dungeoneering)" : Skill(0, False, False, "int"),
            "Knowledge (engineering)"   : Skill(0, False, False, "int"),
            "Knowledge (geography)"     : Skill(0, False, False, "int"),
            "Knowledge (history)"       : Skill(0, False, False, "int"),
            "Knowledge (local)"         : Skill(0, False, False, "int"),
            "Knowledge (nature)"        : Skill(0, False, False, "int"),
            "Knowledge (nobility)"      : Skill(0, False, False, "int"),
            "Knowledge (planes)"        : Skill(0, False, False, "int"),
            "Knowledge (religion)"      : Skill(0, False, False, "int"),
            "Linguistics"               : Skill(0, False, False, "int"),
            "Perception"                : Skill(0, True,  False, "wis"),
            "Perform (act)"             : Skill(0, True,  False, "cha"),
            "Perform (comedy)"          : Skill(0, True,  False, "cha"),
            "Perform (dance)"           : Skill(0, True,  False, "cha"),
            "Perform (keyboard)"        : Skill(0, True,  False, "cha"),
            "Perform (oratory)"         : Skill(0, True,  False, "cha"),
            "Perform (percussion)"      : Skill(0, True,  False, "cha"),
            "Perform (string)"          : Skill(0, True,  False, "cha"),
            "Perform (wind)"            : Skill(0, True,  False, "cha"),
            "Perform (sing)"            : Skill(0, True,  False, "cha"),
            "Profession"                : Skill(0, False, False, "wis"), #TODO
            "Ride"                      : Skill(0, True,  True,  "dex"),
            "Sense Motive"              : Skill(0, True,  False, "wis"),
            "Sleight of Hand"           : Skill(0, False, True,  "dex"),
            "Spellcraft"                : Skill(0, False, False, "int"),
            "Stealth"                   : Skill(0, True,  True,  "dex"),
            "Survival"                  : Skill(0, True,  False, "wis"),
            "Swim"                      : Skill(0, True,  True,  "str"),
            "Use Magic Device"          : Skill(0, False, False, "cha")
        }


    def __getitem__(self, skill):
        return self.tree[skill]