def income(cost, count):
    income = cost * count
    return income


count_a = int(input("Enter count of A seats: "))
count_b = int(input("Enter count of B seats: "))
count_c = int(input("Enter count of C seats: "))
income_a = income(15, count_a)
income_b = income(12, count_b)
income_c = income(9, count_c)
total_income = income_a + income_b + income_c
print(f"Income from class A seats: ${income_a}")
print(f"Income from class B seats: ${income_b}")
print(f"Income from class C seats: ${income_c}")
print(f"Total income: ${total_income}")
