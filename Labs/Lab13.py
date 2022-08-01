import random
random_num = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100...")
guess = count = 0
while guess != random_num:
    guess = int(input("Your guess? "))
    if guess < random_num:
        print("It's higher.")
    elif guess > random_num:
        print("It's lower.")
    count += 1
print(f"You guessed it in {count} guesses!")
