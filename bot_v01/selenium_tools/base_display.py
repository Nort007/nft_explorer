from pyvirtualdisplay import Display
from random import randint


class BaseDisplay:
    def __init__(self, y: int = 800, x: int = 600):
        self.display = Display(size=(y, x))
        self.y = y
        self.x = x

    def start_display(self):
        self.display.start()
