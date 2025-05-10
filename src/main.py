from conversion_helper import *
from pottery_calc_helper import *
from functools import partial
from ui.graphics import Input
import tkinter as tk
from tkinter import Entry

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
    desired_frame = tk.Frame(master=main_frame)
    thrown_frame = tk.Frame(master=main_frame)
    desired_inputs = ["Desired Inner Diameter (inch)", "Desired Inner Height (inch)", "Shrinkage", "Wall Thickness"]
    thrown_inputs = ["Thrown Inner Diameter", "Thrown Inner Height", "Thrown Wall Thickness", "Estimated Clay Weight 🪄"]
    form_builder(desired_inputs, desired_frame)
    form_builder(thrown_inputs, thrown_frame)

    #Add Calculate Button
    button = tk.Button(master=desired_frame, text="Calculate Thrown!", command=partial(calculate_thrown, (desired_frame, thrown_frame)))
    # button.bind("<Button-1>", calculate_thrown) #button 1 means left click
    button.pack()
    desired_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    thrown_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    main_frame.pack()
    window.mainloop()
def form_builder(input_items, frame):
    global inputs
    local_items = []
    for item in input_items:
        new_input = Input(item, frame)
        local_items.append(new_input)
    for item in local_items:
        item.label.pack()
        item.entry.pack()
        inputs.extend(local_items)

def calculate_thrown(frame_tuple):
    print("Calculating!")
    global inputs

    shrinkage, diameter, height, wall_thickness = get_desired_inputs()

    values = inner_inch_dimensions_to_all_values(shrinkage, diameter, height, wall_thickness)
    update_thrown_inputs(values)

def update_thrown_inputs(values):
    global inputs
    diameter, height, wall_thickness, clay_weight = None, None, None, None
    #pull inputs back into local context to only work with desired elements.
    #there has got to be a better way to manage inputs in tkinter 🫠
    for input in inputs:
        if input.name == "Thrown Inner Diameter":
            diameter = input.entry
        if input.name == "Thrown Inner Height":
            height  = input.entry
        if input.name == "Thrown Wall Thickness":
            wall_thickness = input.entry
        if input.name == "Estimated Clay Weight 🪄":
            clay_weight = input.entry
    if diameter:
        diameter.delete(0, tk.END)
        diameter.insert(0,str(values["t_i_diameter"]))
    if height:
        height.delete(0, tk.END)
        height.insert(0,str(values["t_i_height"]))
    if wall_thickness:
        wall_thickness.delete(0, tk.END)
        wall_thickness.insert(0,str(calc_thrown_size(values["shrinkage"], values["wall_thickness"])))
    if clay_weight:
        clay_weight.delete(0, tk.END)
        if values["clay_weight_ounces"] // 16 > 0.0:
            clay_string = f"{values["clay_weight_ounces"] // 16}lb {round(values["clay_weight_ounces"] % 16, 2)}oz"
        else:
            clay_string = f"{round(values["clay_weight_ounces"] % 16, 2)}oz"
        clay_weight.insert(0, clay_string)
def get_desired_inputs():
    global inputs
    shrinkage, diameter, height, wall_thickness  = None, None, None, None
    for input in inputs:
        #shrinkage
        # print(input.name)
        if input.name == "Shrinkage":
            if input.entry.get() is None or input.entry.get() == '':
                shrinkage = 0.12
            else:
                shrinkage = float(input.entry.get())
                if shrinkage > 1:
                    shrinkage = shrinkage / 100
            input.entry.delete(0,tk.END)
            input.entry.insert(0, str(shrinkage))
        #diameter
        if input.name == "Desired Inner Diameter (inch)":
            if input.entry.get() != '':
                diameter = float(input.entry.get())
            else:
                diameter = 1
            input.entry.delete(0,tk.END)
            input.entry.insert(0, str(diameter))

        #height
        if input.name == "Desired Inner Height (inch)":
            if input.entry.get() != '':
                height = float(input.entry.get())
            else:
                height = 1
            input.entry.delete(0,tk.END)
            input.entry.insert(0, str(height))
        #wall_thickness
        if input.name == "Wall Thickness":
            if input.entry.get() is None or input.entry.get() == '':
                wall_thickness = 0.25
            else:
                wall_thickness = float(input.entry.get())
            input.entry.delete(0,tk.END)
            input.entry.insert(0, str(wall_thickness))

    # print(f"shrinkage {shrinkage}")
    # print(f"diameter {diameter}")
    # print(f"height {height}")
    # print(f"wall_thickness {wall_thickness}")
    return shrinkage, diameter, height, wall_thickness
def main():
    window = tk.Tk()
    setup_window(window)
main()

# for Entry elements
# Retrieving text with .get()
# Deleting text with .delete()
# Inserting text with .insert()
