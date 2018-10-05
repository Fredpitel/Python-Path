import ttk
import Tkinter as tk

class LanguageWindow():
    def __init__(self, controller, languages, remaining):
        languageWindow = tk.Toplevel()
        languageWindow.title("Bonus Languages")

        self.remaining = remaining
        self.remainingString = tk.StringVar(value="Add Bonus Language(s) - Remaining: %d" % self.remaining)

        frame = ttk.Frame(languageWindow, relief=tk.RAISED, padding=10)
        frame.pack()
        tk.Label(frame, textvariable=self.remainingString).grid(row=0, column=0, columnspan=2, sticky="EW")
        
        checkboxes = []

        i=2
        for language in languages:
            label = tk.Label(frame, text=language)
            label.config(font=('Helvetica', 10))
            label.grid(row=i, column=0)

            var = tk.IntVar()
            checkbox = tk.Checkbutton(frame, variable=var)
            checkbox.grid(row=i, column=1)
            checkbox.language = language
            checkbox.var = var

            checkboxes.append(checkbox)

            var.trace("w", lambda i,o,x,c=checkbox: self.updateRemaining(c))

            i+=1

        self.addButton = tk.Button(frame, text="Add", command=lambda l=languageWindow, c=checkboxes: controller.addBonusLanguages(l,c))
        self.addButton.grid(row=i, column=0, columnspan=2, pady=10)


    def updateRemaining(self, checkbox):
        if checkbox.var.get():
            self.remaining -= 1
        else:
            self.remaining += 1

        self.remainingString.set("Add Bonus Language(s) - Remaining: %d" % self.remaining)
        
        if self.remaining < 0:
            self.addButton.config(state="disabled")
        else:
            self.addButton.config(state="normal")