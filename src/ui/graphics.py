from tkinter import Tk, Canvas

# x=0 is left of screen
# y=0 is top of screen
# 0,0 is top left of screen
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Pottery Calculator")
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.__running = False
