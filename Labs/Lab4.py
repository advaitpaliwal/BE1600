import random
weight = random.choice(range(1, 51))

shipping_rate = 0

if weight < 3:
    shipping_rate = 1.1
elif weight < 7:
    shipping_rate = 2.2
elif weight < 11:
    shipping_rate = 3.7
elif weight < 21:
    shipping_rate = 4.5

print(f"Package weight: {weight}")

if shipping_rate != 0:
    print(f"Shipping rate: ${shipping_rate}")
    print(f"Shipping charge: ${shipping_rate*weight}")
else:
    print("The package is over 20 pounds and cannot be shipped")
