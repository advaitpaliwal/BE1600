def km_to_miles(km):
    return km * 0.6214


km = float(input("Enter the distance in kilometers: "))
miles = km_to_miles(km)
print(f"The conversion of {km} kilometers to miles is {miles} miles.")
