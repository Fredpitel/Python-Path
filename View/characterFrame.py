#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ttk
import Tkinter as tk

class CharacterFrame():
    def __init__(self, controller, parent):
        self.controller =controller

        self.characterFrame = ttk.Frame(parent)
        self.characterFrame.grid(row=0, column=0, sticky="NSEW")
        self.characterFrame.grid_rowconfigure(0, weight=1)
        self.characterFrame.grid_columnconfigure(0, weight=1)
        
        tk.Button(self.characterFrame, text="×", font=("helvetica", 12), command=self.controller.closeTab).grid(row=0, column=1, padx=5, sticky="NE")