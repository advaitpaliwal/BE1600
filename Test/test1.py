#2, 3, 5, 7, 11, 13, 17, 19
# prime is a number that doesn't have multiple except itself
from math import isqrt


def isprime(x):
    if x <= 1:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True


i = 0
while True:
    if isprime(i):
        print(i)
    i += 1
