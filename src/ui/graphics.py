import tkinter as tk

# x=0 is left of screen
# y=0 is top of screen
# 0,0 is top left of screen
class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title("Pottery Calculator")
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        self.__running = False
class Input:
    def __init__(self, name, frame = None, width = 40):
        self.name = name
        self.label = tk.Label(master=frame, text=name)
        self.entry = tk.Entry(master=frame, width=width)
