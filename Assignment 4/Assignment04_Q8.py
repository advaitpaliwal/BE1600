def print_average():
    avg = 0
    num_list = []
    data = float(input("Type a number: "))
    num_list.append(data)
    while True:
        data = float(input("Type a number: "))
        if data < 0:
            break
        num_list.append(data)

    avg = sum(num_list) / len(num_list)
    print(f"Average was {avg}")


print_average()
