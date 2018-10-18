import ttk
import Tkinter as tk

class Splash:
    def __init__(self, parent):
        self.splash = ttk.Frame(parent)
        self.splash.grid(row=0, column=0, sticky="NSEW")

        frame = tk.Frame(self.splash)
        tk.Label(frame, text="Loading, please wait").pack(expand=True, fill="both")

        frame.pack(expand=True, fill="both")


    def destroy(self):
        self.splash.destroy()