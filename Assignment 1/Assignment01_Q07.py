import math

wall_space = float(input("Enter wall space in square feet: "))
paint_price = float(input("Enter paint price per gallon: "))
gallons_paint = math.ceil(wall_space / 115)
hour_labor = 8 * gallons_paint
paint_charge = paint_price * gallons_paint
labor_charge = 20 * hour_labor
total_cost = paint_charge + labor_charge

print(f"Gallons of paint: {gallons_paint}")
print(f"Hours of labor: {hour_labor}")
print(f"Paint charges: {paint_charge}")
print(f"Total cost: {total_cost}")
