while True:
    first = float(input("Enter a number: "))
    second = float(input("Enter another number: "))
    print(f"The sum of the numbers you entered is {first+second}")
    ask = str(input("Do you want to do that again? (y/n): "))
    if ask.lower() == "n":
        break
