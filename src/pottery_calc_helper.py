def calc_thrown_size(desired_size, shrinkage):
    #formula desired_size/(1 - shrinkage) = thrown size
    thrown_size = desired_size / (1 - shrinkage)
    return round(thrown_size, 2)

print(f"calc_thrown_size(4): {calc_thrown_size(4, 0.12)}")
