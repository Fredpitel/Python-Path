import Tkinter as tk

class Splash:
    def __init__(self):
        self.splash = tk.Tk()
        self.splash.attributes("-topmost", True, "-zoomed", True)
        self.splash.title("loading")

        frame = tk.Frame(self.splash)
        tk.Label(frame, text="Loading, please wait").pack(expand=True, fill="both")

        frame.pack(expand=True, fill="both")


    def destroy(self):
        self.splash.destroy()