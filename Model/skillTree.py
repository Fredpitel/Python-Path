from Modifiable import Skill

class SkillTree:
    def __init__(self, char):
        self.tree = {
            "Acrobatics"                : Skill(char, 0, True,  True,  "dex"),
            "Appraise"                  : Skill(char, 0, True,  False, "int"),
            "Bluff"                     : Skill(char, 0, True,  False, "cha"),
            "Climb"                     : Skill(char, 0, True,  True,  "str"),
            "Craft"                     : Skill(char, 0, True,  False, "int"), #TODO
            "Diplomacy"                 : Skill(char, 0, True,  False, "cha"),
            "Disable Device"            : Skill(char, 0, False, True,  "dex"),
            "Disguise"                  : Skill(char, 0, True,  False, "cha"),
            "Escape Artist"             : Skill(char, 0, True,  True,  "dex"),
            "Fly"                       : Skill(char, 0, True,  True,  "dex"),
            "Handle Animal"             : Skill(char, 0, False, False, "cha"),
            "Heal"                      : Skill(char, 0, True,  False, "wis"),
            "Intimidate"                : Skill(char, 0, True,  False, "cha"),
            "Knowledge (arcana)"        : Skill(char, 0, False, False, "int"),
            "Knowledge (dungeoneering)" : Skill(char, 0, False, False, "int"),
            "Knowledge (engineering)"   : Skill(char, 0, False, False, "int"),
            "Knowledge (geography)"     : Skill(char, 0, False, False, "int"),
            "Knowledge (history)"       : Skill(char, 0, False, False, "int"),
            "Knowledge (local)"         : Skill(char, 0, False, False, "int"),
            "Knowledge (nature)"        : Skill(char, 0, False, False, "int"),
            "Knowledge (nobility)"      : Skill(char, 0, False, False, "int"),
            "Knowledge (planes)"        : Skill(char, 0, False, False, "int"),
            "Knowledge (religion)"      : Skill(char, 0, False, False, "int"),
            "Linguistics"               : Skill(char, 0, False, False, "int"),
            "Perception"                : Skill(char, 0, True,  False, "wis"),
            "Perform (act)"             : Skill(char, 0, True,  False, "cha"),
            "Perform (comedy)"          : Skill(char, 0, True,  False, "cha"),
            "Perform (dance)"           : Skill(char, 0, True,  False, "cha"),
            "Perform (keyboard)"        : Skill(char, 0, True,  False, "cha"),
            "Perform (oratory)"         : Skill(char, 0, True,  False, "cha"),
            "Perform (percussion)"      : Skill(char, 0, True,  False, "cha"),
            "Perform (string)"          : Skill(char, 0, True,  False, "cha"),
            "Perform (wind)"            : Skill(char, 0, True,  False, "cha"),
            "Perform (sing)"            : Skill(char, 0, True,  False, "cha"),
            "Profession"                : Skill(char, 0, False, False, "wis"), #TODO
            "Ride"                      : Skill(char, 0, True,  True,  "dex"),
            "Sense Motive"              : Skill(char, 0, True,  False, "wis"),
            "Sleight of Hand"           : Skill(char, 0, False, True,  "dex"),
            "Spellcraft"                : Skill(char, 0, False, False, "int"),
            "Stealth"                   : Skill(char, 0, True,  True,  "dex"),
            "Survival"                  : Skill(char, 0, True,  False, "wis"),
            "Swim"                      : Skill(char, 0, True,  True,  "str"),
            "Use Magic Device"          : Skill(char,0, False, False, "cha")
        }


    def __getitem__(self, skill):
        return self.tree[skill].value

