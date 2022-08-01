import math


def sphere_volume(r):
    return 4 / 3 * math.pi * r ** 3


radius = float(input("Enter the radius of a sphere: "))
print(sphere_volume(radius))

# 4/3 pi r^3
