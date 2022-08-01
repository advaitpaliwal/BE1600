import random


def three_heads():
    all_flips = []
    sides = ["H", "T"]
    while len(all_flips) < 3 or all_flips[-3:] != [1, 1, 1]:
        flip = random.randint(0, 1)
        all_flips.append(flip)
        if flip == 1:
            print("H", end=" ")
        else:
            print("T", end=" ")
    print("\nThree heads in a row!")


three_heads()
