import math

#basic conversions
def inches_to_cm(inches):
    pass
def cm_to_inches(cm):
    pass

#volume calculations
def volume_cube(length):
    volume_rect_prism(length, length, length)

def volume_rect_prism(length, width, height):
    return length * width * height

def volume_cylinder_radius(radius, height):
    #volume = π(r^2)h
    volume = math.pi * (radius ** 2) * height
    return volume

def volume_cylinder_diameter(diameter, height):
    radius = diameter/2
    volume = volume_cylinder_radius(radius, height)
    return volume

def clay_volume(inner_diameter, inner_height, wall_thickness, base_thickness = None):
    if base_thickness == None:
        base_thickness = wall_thickness
    outer_diameter = inner_diameter + (wall_thickness * 2)
    outer_height = inner_height + base_thickness


    pass
