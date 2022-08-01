import random
wins = 0
flips = 0
while True:
    random_num = random.randint(1, 2)
    number_input = int(
        input("Enter 1 for Head\nEnter 2 for Tail\nEnter 9 to exit\n"))
    if number_input == 9:
        print(f"Number of flips {flips}")
        print(f"You Won {wins} Time(s)")
        break
    if random_num == number_input:
        print("You Won")
        wins += 1
    else:
        print("You Lost")
    flips += 1
