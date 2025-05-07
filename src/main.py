from conversion_helper import *
from pottery_calc_helper import *
from functools import partial
from ui.graphics import Input
import tkinter as tk

# def get_text():
#     text = entry.get()
#     print("You entered:", text)

# def get_num():
#     my_num = float(entry.get())
#     print("You entered:", my_num)

inputs = []

def setup_window(window):
    window.title("Pottery Calculator")
    main_frame = tk.Frame()

    #Desired Size Input items
    desired_frame = tk.Frame(master=window, width=40)

    #
    thrown_frame = tk.Frame()
    build_desired_frame(desired_frame)
    build_thrown_frame(thrown_frame)

    #Add Calculate Button


    button = tk.Button(master=desired_frame, text="Calculate Thrown!", command=partial(calculate_thrown, (desired_frame, thrown_frame)))
    # button.bind("<Button-1>", calculate_thrown) #button 1 means left click
    button.pack()
    desired_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    thrown_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    main_frame.pack()
    window.mainloop()
def build_desired_frame(desired_frame):
    ui_items = []
    lbl_diameter = tk.Label(master=desired_frame, text="Desired Inner Diameter")
    ent_diameter = tk.Entry(master=desired_frame, width=40)
    ui_items.append((lbl_diameter, ent_diameter))
    lbl_height = tk.Label(master=desired_frame, text="Desired Inner Height")
    ent_height = tk.Entry(master=desired_frame, width=40)
    ui_items.append((lbl_height, ent_height))
    lbl_shrinkage = tk.Label(master=desired_frame, text="Shrinkage")
    ent_shrinkage = tk.Entry(master=desired_frame, width=40)
    ent_shrinkage.insert(0,"0.12")
    ui_items.append((lbl_shrinkage, ent_shrinkage))
    lbl_thickness = tk.Label(master=desired_frame, text="Wall Thickness")
    ent_thickness = tk.Entry(master=desired_frame, width=40)
    ent_thickness.insert(0, "0.25")
    ui_items.append((lbl_thickness, ent_thickness))

    for item in ui_items:
        item[0].pack()
        item[1].pack()
def build_thrown_frame(thrown_frame):
    ui_items = []

    lbl_diameter = tk.Label(master=thrown_frame, text="Thrown Diameter")
    ent_diameter = tk.Entry(master=thrown_frame, width=40)
    ui_items.append((lbl_diameter, ent_diameter))
    lbl_height = tk.Label(master=thrown_frame, text="Thrown Inner Height")
    ent_height = tk.Entry(master=thrown_frame, width=40)
    ui_items.append((lbl_height, ent_height))
    lbl_thickness = tk.Label(master=thrown_frame, text="Thrown Wall Thickness")
    ent_thickness = tk.Entry(master=thrown_frame, width=40)
    # ent_thickness.insert(0, "0.25")
    ui_items.append((lbl_thickness, ent_thickness))
    for item in ui_items:
        item[0].pack()
        item[1].pack()

def calculate_thrown(frame_tuple):
    print("Calculating!")
    desired_frame = frame_tuple[0]
    thrown_frame = frame_tuple[1]

    # for widget in desired_frame.winfo_children():
    #     if isinstance(widget, tk.Entry)
    # #shrinkage, d_inner_diam, d_inner_height, d_wall_thickness, d_base_thickness
    # shrinkage =
    # d_i_diam =
    # d_i_height =
    # wall_thickness =
    # d_base_thickness =
    # inner_inch_dimensions_to_all_values

def main():
    window = tk.Tk()
    setup_window(window)
main()

# for Entry elements
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
