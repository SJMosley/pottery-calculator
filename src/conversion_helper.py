import math

#ref sites
#https://www.rapidtables.com/convert/index.html
#AMAZING THING: 1 cubic centimeter = 1 milliliter

#constants
US_OZ_ML = 29.573529
UK_OZ_ML = 28.4130625

#basic conversions (same type units)
def inches_to_cm(inches):
    #centimeters = inches × 2.54
    return inches * 2.54
def cm_to_inches(cm):
    #inches = centimeters / 2.54
    return cm / 2.54
def ml_to_oz(ml):
    # 1 fluid ounce (US) = 29.573529562 milliliter
    return ml / US_OZ_ML
def oz_to_ml(oz):
    # 1 fluid ounce (US) = 29.573529562 milliliter
    return oz * US_OZ_ML
def oz_to_pounds(oz):
    pass
def pounds_to_oz(pound):
    pass
def oz_to_grams(oz):
    pass
def grams_to_oz(gram):
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

def volume_difference_inner(inner_diameter, inner_height, wall_thickness, base_thickness = None):
    #the volume difference can be used to calculate how much clay is necessary for the piece
    if base_thickness == None:
        base_thickness = wall_thickness
    outer_diameter = inner_diameter + (wall_thickness * 2)
    outer_height = inner_height + base_thickness
    outer_volume = volume_cylinder_diameter(outer_diameter, outer_height)
    inner_volume = volume_cylinder_diameter(inner_diameter, inner_height)
    volume_difference = outer_volume - inner_volume

    return volume_difference

#estimation functions
def estimate_wall_thickness(diameter, height):
    pass

#conversions (different types, e.g. volume -> weight, volume -> oz, etc.)
def volume_to_oz(volume, units = None):
    if units is None:
        units = "cm"
    pass
def volume_to_ml(volume, units = None):
    if units is None:
        units = "cm"
    pass
def oz_to_volume():
    pass
def ml_to_volume():
    pass

#Surface Area (FUTURE, potential glaze cost calculator)
#https://www.calculator.net/surface-area-calculator.html
