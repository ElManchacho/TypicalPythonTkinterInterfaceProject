from tkinter import *
from typing import Any
from screeninfo import get_monitors

class Screen:

    resolution : get_monitors

    window : Tk

    def __init__(self) -> None:
        
        self.resolution = get_monitors()[0]

        self.window = Tk()

        w = self.resolution.width
        h = self.resolution.height

        self.window.geometry('%dx%d+%d+%d' % (w, h, 0, 0))
        
        # At this point, the screen is a blank 1920/1080 white page

    def displayScreen(self) -> None:

        self.window.mainloop()
