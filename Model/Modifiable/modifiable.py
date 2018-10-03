import Tkinter as tk

from decimal import Decimal

__metaclass__ = type

class Modifiable():
    STACKABLE_TYPES = ["dodge", "untyped"]

    def __init__(self, baseValue):
        self.baseValue = tk.IntVar(value=baseValue)
        self.value     = tk.IntVar(value=baseValue)
        self.modValue  = tk.IntVar(value=0)
        self.modifiers = {}

        self.value.trace("w", lambda i,o,x: self.update())
        self.baseValue.trace("w", lambda i,o,x: self.update())


    def addModifier(self, mod, source, toggler):
        if mod["type"] in self.modifiers:
            self.modifiers[mod["type"]].append((source, mod["value"]))
        else:
            self.modifiers[mod["type"]] = [(source, mod["value"])]

        source.trace("w", lambda i,o,x,s=source: self.removeModifier(s))
        
        if toggler is not None:
            toggler.bind("<Unmap>", lambda e, source=source: self.removeModifier(source))
        
        self.update()


    def removeModifier(self, source):
        for type in self.modifiers.keys():
            for modSource in self.modifiers[type]:
                if modSource[0] == source:
                    self.modifiers[type].remove(modSource)

                    if not self.modifiers[type]:
                        del self.modifiers[type]

        self.update()


    def update(self):
        self.modValue.set(self.getModValue())
        self.value.set(self.baseValue.get() + self.modValue.get())


    def getModValue(self):
        total = 0
        for type in self.modifiers.keys():
            if type in self.STACKABLE_TYPES:
                for source in self.modifiers[type]:
                    total += source[1]
            else:
                maxMod = ("", Decimal('-Infinity'))
                for source in self.modifiers[type]:
                    if source[1] > maxMod[1] and source[0] != maxMod[0]:
                        maxMod = source

                total += maxMod[1]

        return total