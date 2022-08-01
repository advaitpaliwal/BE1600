def inCircle(point_x, point_y, radius):
    return ((point_x * point_x + point_y * point_y) <= radius * radius)


point_x = int(input("What is the x value of the point? "))
point_y = int(input("What is the y value of the point? "))
radius = int(input("What is the radius of the circle? "))

circle = inCircle(point_x, point_y, radius)

if circle:
    print(f"Point ( {point_x}, {point_y} ) is in circle with radius {radius}")
else:
    print(
        f"Point ( {point_x}, {point_y} ) is not in circle with radius {radius}")
