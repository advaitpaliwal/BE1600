list_L = []
for i in range(5):
    number_input = int(input("Enter a number "))
    list_L.append(number_input)


def even_odd(list):
    list_E = []
    list_O = []
    for number in list:
        if number % 2 == 0:
            list_E.append(str(number))
        else:
            list_O.append(str(number))
    even_nums = " ".join(list_E)
    odd_nums = " ".join(list_O)
    return f"List L: {list}\nEven numbers: {even_nums}\nOdd numbers: {odd_nums}"


print(even_odd(list_L))
