from pyvirtualdisplay import Display


class BaseDisplay:
    def __init__(self, y: int = 800, x: int = 600):
        self.display = Display(size=(y, x))
        self.y = y
        self.x = x

    def start_display(self):
        self.display.start()
        self.stop_display()

    def stop_display(self):
        self.display.stop()
