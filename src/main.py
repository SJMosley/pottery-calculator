from conversion_helper import *
# from ui.graphics import Window
import tkinter as tk

def setup_window(window):
    window.title("Pottery Calculator")
    main_frame = tk.Frame()
    main_frame.pack()
    #Desired Size Input items
    # desired_frame = tk.Frame()
    # desired_frame.pack()
    # thrown_frame = tk.Frame()
    # thrown_frame.pack()
    ui_items = []
    label_diameter = tk.Label(text="Desired Inner Diameter")
    entry_diameter = tk.Entry()
    ui_items.append((label_diameter, entry_diameter))
    label_height = tk.Label(text="Desired Inner Height")
    entry_height = tk.Entry()
    ui_items.append((label_height, entry_height))
    label_shrinkage = tk.Label(text="Shrinkage")
    entry_shrinkage = tk.Entry()
    ui_items.append((label_shrinkage, entry_shrinkage))
    label_thickness = tk.Label(text="Wall Thickness")
    entry_thickness = tk.Entry()
    ui_items.append((label_thickness, entry_thickness))

    for item in ui_items:
        item[0].pack()
        item[1].pack()

    #Add Calculate Button

    window.mainloop()

def main():
    window = tk.Tk()
    setup_window(window)
main()

# for Entry elements
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
