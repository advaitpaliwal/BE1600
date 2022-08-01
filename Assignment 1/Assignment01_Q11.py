A = 5
B = 10


def func1(range1, range2):
    Sum = 0
    for i in range(range1, range2 + 1):
        print(i, end=" ")
        Sum = Sum + i
    print(f"\nsum of numbers: {Sum}")


func1(A, B)

print(f"\nsum of numbers: ")
