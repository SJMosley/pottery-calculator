import math

#ref sites
#https://www.rapidtables.com/convert/index.html
#AMAZING THING: 1 cubic centimeter = 1 milliliter

#constants relationships
US_OZ_ML = 29.573529
UK_OZ_ML = 28.4130625
OZ_GM = 28.349523125
INCH_CM = 2.54
POUND_OZ = 16

#basic conversions (same type units)
def inches_to_cm(inches):
    #centimeters = inches × 2.54
    return inches * INCH_CM
def cm_to_inches(cm):
    #inches = centimeters / 2.54
    return cm / INCH_CM
def inch_to_fluid_oz(inch_volume):
    return inch_volume * 0.554113
def fluid_oz_to_inch(fl_oz):
    return fl_oz / 0.554113
def ml_to_oz(ml):
    # 1 fluid ounce (US) = 29.573529562 milliliter
    return ml / US_OZ_ML
def oz_to_ml(oz):
    # 1 fluid ounce (US) = 29.573529562 milliliter
    return oz * US_OZ_ML
def oz_to_pounds(oz):
    #16 ounce = 1 pound
    return oz / POUND_OZ
def pounds_to_oz(pound):
    #16 ounce = 1 pound
    return pound * POUND_OZ
def oz_to_grams(oz):
    #1 ounce = 28.349523125 gram
    return oz * OZ_GM
def grams_to_oz(gram):
    #1 ounce = 28.349523125 gram
    return gram / OZ_GM

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

#conversions (different types, e.g. volume + density -> weight, volume -> oz, etc.)
def volume_to_weight_oz(volume, units, density):
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

#density = mass/volume
#Weight (grams) = Volume (mL) × Density (g/mL)
#1.8 (g/cm^3)
#1.8 (g/mL^3)
