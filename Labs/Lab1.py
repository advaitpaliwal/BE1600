from math import sqrt

list = []

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))


def average(num1, num2, num3, num4, num5):
    list.extend([num1, num2, num3, num4, num5])
    avg = sum(list) / len(list)
    return avg


avg = average(num1, num2, num3, num4, num5)
print("Average =", avg)


def std_dev():
    numerator = 0
    for number in list:
        numerator += (number - avg)**2
    std_dev = sqrt(numerator / len(list))
    return std_dev


sd = std_dev()
print("Standard Deviation =", sd)
