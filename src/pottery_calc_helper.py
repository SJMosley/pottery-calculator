from conversion_helper import *
def calc_thrown_size(shrinkage, desired_size):
    #formula desired_size/(1 - shrinkage) = thrown size
    thrown_size = desired_size / (1 - shrinkage)
    return round(thrown_size, 2)
def calc_desired_size(shrinkage, thrown_size):
    desired_size = thrown_size * (1 - shrinkage)
    return desired_size

def thrown_dimensions_to_all_values(shrinkage, t_o_diameter, t_o_height, d_wall_thickness, d_base_thickness = None):
    values = {
        "shrinkage": shrinkage,
        "t_o_diameter": t_o_diameter,
        "t_o_height": t_o_height,
        "wall_thickness": d_wall_thickness,
        "base_thickness": d_base_thickness,
    }
    thrown_wall_thickness = calc_thrown_size(shrinkage, d_wall_thickness)
    values["t_i_diameter"] = t_o_diameter - (2 * thrown_wall_thickness)
    if d_base_thickness:
        thrown_base_thickness = calc_thrown_size(shrinkage, d_base_thickness)
    else:
        thrown_base_thickness = thrown_wall_thickness
    values["t_i_height"] = t_o_height - thrown_base_thickness
    values["d_o_diameter"] = calc_desired_size(shrinkage, values["t_o_diameter"])
    values["d_o_height"] = calc_desired_size(shrinkage, values["t_o_height"])
    values["d_i_diameter"] = calc_desired_size(shrinkage, values["t_i_diameter"])
    values["d_i_height"] = calc_desired_size(shrinkage, values["t_i_height"])
    values["desired_volume"] = volume_cylinder_diameter(values["d_i_diameter"], values["d_i_height"])
    values["desired_outer_volume"] = volume_cylinder_diameter(values["d_o_diameter"], values["d_o_height"])

    #1 inch³ = 16.387 cm³ = 16.387 mL
    #(since 1 mL = 1 cm³)
    values["thrown_inner_volume"] = volume_cylinder_diameter(values["t_i_diameter"], values["t_i_height"])
    values["thrown_outer_volume"] = volume_cylinder_diameter(values["t_o_diameter"], values["t_o_height"])
    values["total_thrown_volume"] = values["thrown_outer_volume"] - values["thrown_inner_volume"]

    thrown_volume_cm3 = values["total_thrown_volume"] * 16.387
    #1.8 (g/cm^3)
    density_per_cm3 = 1.8
    #Weight (grams) = Volume (mL) × Density (g/mL)
    values["clay_weight_grams"] = thrown_volume_cm3 * density_per_cm3
    values["clay_weight_ounces"] = grams_to_oz(values["clay_weight_grams"])
    return values

def inner_inch_dimensions_to_all_values(shrinkage, d_inner_diameter, d_inner_height, d_wall_thickness, d_base_thickness = None):
    values = {
        "shrinkage": shrinkage,
        "d_i_diameter": d_inner_diameter,
        "d_i_height": d_inner_height,
        "wall_thickness": d_wall_thickness,
        "base_thickness": d_base_thickness
    }

    values["d_o_diameter"] = d_inner_diameter + (2 * d_wall_thickness)
    if d_base_thickness:
        values["d_o_height"] = d_inner_height + d_base_thickness
    else:
        values["d_o_height"] = d_inner_height + d_wall_thickness

    values["desired_volume"] = volume_cylinder_diameter(values["d_i_diameter"], values["d_i_height"])
    values["desired_outer_volume"] = volume_cylinder_diameter(values["d_o_diameter"], values["d_o_height"])
    # thrown_wall_thickness = calc_thrown_size(shrinkage, d_wall_thickness)
    values["t_i_diameter"] = calc_thrown_size(shrinkage, values["d_i_diameter"])
    values["t_i_height"] = calc_thrown_size(shrinkage, values["d_i_height"])
    values["t_o_diameter"] = calc_thrown_size(shrinkage, values["d_o_diameter"])
    values["t_o_height"]= calc_thrown_size(shrinkage, values["d_o_height"])

    #1 inch³ = 16.387 cm³ = 16.387 mL
    #(since 1 mL = 1 cm³)
    values["thrown_inner_volume"] = volume_cylinder_diameter(values["t_i_diameter"], values["t_i_height"])
    values["thrown_outer_volume"] = volume_cylinder_diameter(values["t_o_diameter"], values["t_o_height"])
    values["total_thrown_volume"] = values["thrown_outer_volume"] - values["thrown_inner_volume"]

    thrown_volume_cm3 = values["total_thrown_volume"] * 16.387
    #1.8 (g/cm^3)
    density_per_cm3 = 1.8
    #Weight (grams) = Volume (mL) × Density (g/mL)
    values["clay_weight_grams"] = thrown_volume_cm3 * density_per_cm3
    values["clay_weight_ounces"] = grams_to_oz(values["clay_weight_grams"])
    return values
def output(values):
    print(f"""
    DESIRED SIZE
    INNER (Diameter x Height):
        Diameter:       {values["d_i_diameter"]} inches
        Height:         {values["d_i_height"]} inches
        Wall Thickness: {values["wall_thickness"]} inches
    -----------------------------
    OUTER (Diameter x Height):
        Diameter:       {values["d_i_diameter"]} inches
        Height:         {values["d_i_height"]} inches
    VOLUME (liquid):
        Volume (oz):    {inch_to_fluid_oz(values["desired_volume"])}

    THROWN SIZE 🏺
    DESIRED SIZE
    INNER (Diameter x Height):
        Diameter:       {values["t_i_diameter"]} inches
        Height:         {values["t_i_height"]} inches
        Wall Thickness: {values["wall_thickness"]} inches
    -----------------------------
    OUTER (Diameter x Height):
        Diameter:       {values["t_o_diameter"]} inches
        Height:         {values["t_o_height"]} inches
    INNER VOLUME (liquid):
        Volume (oz):    {values["desired_volume"]}
    ✨✨ Estimated Clay Weight: ✨✨
            {values["clay_weight_ounces"] // 16}lb {round(values["clay_weight_ounces"] % 16, 2)}oz

    """)
def quick_test(values, expected, inner_volume = None):
    estimated = f"{int(values["clay_weight_ounces"] // 16)}lbs. {round(values["clay_weight_ounces"] % 16,2)}oz."
    print(f"{estimated} :: {expected}")
def long_test(values, expected, inner_volume = None):
    print(f"""
    DESIRED SIZE
    INNER (Diameter x Height):
        Diameter:       {values["d_i_diameter"]} inches
        Height:         {values["d_i_height"]} inches
        Wall Thickness: {values["wall_thickness"]} inches
    -----------------------------
    OUTER (Diameter x Height):
        Diameter:       {values["d_i_diameter"]} inches
        Height:         {values["d_i_height"]} inches
    VOLUME (liquid):
        Volume (oz):    {inch_to_fluid_oz(values["desired_volume"])}
        Chart inner Volume {inner_volume}

    THROWN SIZE 🏺
    DESIRED SIZE
    INNER (Diameter x Height):
        Diameter:       {values["t_i_diameter"]} inches
        Height:         {values["t_i_height"]} inches
        Wall Thickness: {values["wall_thickness"]} inches
    -----------------------------
    OUTER (Diameter x Height):
        Diameter:       {values["t_o_diameter"]} inches
        Height:         {values["t_o_height"]} inches
    INNER VOLUME (liquid):
        Volume (oz):    {values["desired_volume"]}
    ✨✨ Estimated Clay Weight: ✨✨
    Estimated:{values["clay_weight_ounces"] // 16}lb {round(values["clay_weight_ounces"] % 16, 2)}oz
    Expected: {expected}

    """)
##TESTING
# print(f"calc_thrown_size(4): {calc_thrown_size(4, 0.12)}")
run_cases = [
    # inner_inch_dimensions_to_all_values(0.12, 4, 4, 0.25),
    # inner_inch_dimensions_to_all_values(0.12, 2, 2, 0.25),
    # inner_inch_dimensions_to_all_values(0.12, 8, 8, 0.25),
    (thrown_dimensions_to_all_values(0.12, 3, 3, 0.25), "10oz", "6oz"),
    # (thrown_dimensions_to_all_values(0.12, 3, 5, 0.25), "14oz", "8oz"),
    (thrown_dimensions_to_all_values(0.12, 3.5, 7, 0.25), "1lb 5oz", "14oz"),
    # (thrown_dimensions_to_all_values(0.12,5.5, 1, 0.25),"13oz"),
    # (thrown_dimensions_to_all_values(0.12,11.5, 1.25, 0.25),"4lb"),
    # (thrown_dimensions_to_all_values(0.12,10, 1.25, 0.25),"3lb"),
    # (thrown_dimensions_to_all_values(0.12,8, 1, 0.25),"2lb 3oz"),
    # (thrown_dimensions_to_all_values(0.12,6.5, .75, 0.25),"1lb 5oz"),
    # (thrown_dimensions_to_all_values(0.12,12, 6, 0.25),"5lb 12oz"),
    # (thrown_dimensions_to_all_values(0.12,10.0, 4.5, 0.25),"4lb 4.5oz"),
    # (thrown_dimensions_to_all_values(0.12,12, 8, 0.25),"5lb 12oz"),
    # (thrown_dimensions_to_all_values(0.12,8.5, 4.5, 0.25),"4lb"),
    # (thrown_dimensions_to_all_values(0.12,6.5, 4, 0.25),"2lb 3oz"),
    # (thrown_dimensions_to_all_values(0.12,6.5, 4, 0.25),"14oz"),
    # (thrown_dimensions_to_all_values(0.12, 4.0, 6.5, 0.25), "1 lb. 8 oz."),
    (thrown_dimensions_to_all_values(0.12, 6.0, 14.0, 0.25), "5 lb. 12 oz."),
    (thrown_dimensions_to_all_values(0.12, 8.0, 8.0, 0.25), "4 lb. 6 oz."),
    # (thrown_dimensions_to_all_values(0.12, 6.0, 6.0, 0.25), "3 lb. 6 oz."),
    # (thrown_dimensions_to_all_values(0.12, 5.0, 4.5, 0.25), "2 lb. 3 oz."),
    # (thrown_dimensions_to_all_values(0.12, 12.0, 4.0, 0.25), "4 lb. 6 oz."),
    # (thrown_dimensions_to_all_values(0.12, 5.0, 8.0, 0.25), "2 lb. 11 oz."),
    # (thrown_dimensions_to_all_values(0.12, 5.0, 12.0, 0.25), "5 lb."),        # assumed oz. missing
    # (thrown_dimensions_to_all_values(0.12, 4.0, 10.0, 0.25), "3 lb. 6 oz."),
    # (thrown_dimensions_to_all_values(0.12, 5.0, 7.0, 0.25), "3 lb. 4 oz."),
    # (thrown_dimensions_to_all_values(0.12, 6.0, 9.0, 0.25), "5 lb. 8 oz."),
]

# print(f"Estimated :: Expected")
# for case in run_cases:
#     long_test(*case)
    # quick_test(*case)

# Finished Item, Clay's weight, Height Width
# After Firing * Ibs./oz. *** inches ** inches **
# 6 oz. coffee mug 10 oz. 3.0 3.0
# 8 oz. coffee mug 14 oz. 5.0 3.0
# 14 oz. beer mug 1 lb. 5 oz. 7.0 3.5
# Saucer 13 oz. 1.0 5.5
# Large dinner plate 4 lb. 1.25 11.5
# ✅ Medium dinner plate 3 lb. 1.0 10.0
# Side plate 2 lb. 3 oz. 1.0 8.0
# Bread and butter plate 1 lb. 5 oz. 75 6.5
# Large bowl 5 lb. 12 oz. 6.0 12.0
# Medium bowl 4 lb. 4.5 10.0
# Small bowl 1 lb. 6 oz. 3.0 6.0
# ✅Large mixing bowl 4 lb. 4.5 10.0
# 4 quart casserole 5 lb. 12 oz. 8.0 12.0
# 2 quart casserole 4 lb. 4.5 8.5
#✅ 1 quart casserole 2lb. 3 oz. 4.0 6.5
# cream pitcher 14 oz. 5.0 3.0
# Finished Item, Clay's weight, Height Width
# 1 pint pitcher 1 lb. 8 oz. 6.5 4.0
# 4 pint pitcher 5 lb. 12 oz. 14.0 6.0
# Large teapot 4 lb. 6 oz. 8.0 8.0
# Medium teapot 3 lb. 6 oz. 6.0 6.0
# Small teapot 2 lb. 3 oz. 4.5 5.0
# 1 liter wine decanter 4 lb. 6 oz. 12.0
# Small wine decanter 2 lb. 11 oz. 8.0 5.0
# Large storage jar 5 lb. 12.0 5.0
# Medium storage jar 3 lb. 6 oz. 10.0 4.0
# Cylinder 1 3 lbs 4 oz. 7.0 5.0
# Cylinder 2 5 lbs 8 oz. 9.0 6.0
