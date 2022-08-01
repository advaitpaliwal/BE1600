import random
num_even = 0
num_odd = 0
for i in range(1, 101):
    rand_num = random.randint(1, 100)
    if rand_num % 2 == 0:
        num_even += 1
    else:
        num_odd += 1
print(
    f"Out of {i} random numbers, {num_odd} were odd and, {num_even} were even.")
