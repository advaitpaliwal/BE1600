import random


def dice_sum(desire):

    while True:
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        total = first + second
        print(f"{first} and {second} = {total}")
        if total == desire:
            break


desire = int(input("Desired dice sum: "))
dice_sum(desire)
