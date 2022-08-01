import random
file_name = str(
    input("Enter the name of the file to which results should be written: "))
how_many = int(
    input("Enter the number of random numbers to be written to the file: "))
with open(file_name, "w") as f:
    for i in range(how_many):
        f.write(f"{random.randint(1, 100)}\n")
