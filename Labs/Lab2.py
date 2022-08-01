def func1(n):
    print("print Numbers Forward:")
    for i in range(1, n + 1):
        print(i, end=" ")


n = int(input("Enter a number "))
func1(n)


def func2(n):
    print("\nprint Numbers Backward:")
    for i in range(n, 0, -1):
        print(i, end=" ")


func2(n)


def func3(n):
    sum_of_odd = 0
    for i in range(n + 1):
        if i % 2 != 0:
            sum_of_odd = sum_of_odd + i
    print("\nsum of odd numbers: " + str(sum_of_odd))


func3(n)


def func4(n):
    sum_of_even = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum_of_even = sum_of_even + i
    print("sum of even numbers: " + str(sum_of_even))


func4(n)
