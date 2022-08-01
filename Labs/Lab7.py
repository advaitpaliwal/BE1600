import random

num_list = []
k = random.randint(1, 10)

print(f"Enter {k} values: ")
for i in range(1, k + 1):
    input_num = int(input(f"Enter value {i}: "))
    num_list.append(input_num)

print(f"original list {num_list}")


def is_sorted(my_list):
    return sorted(my_list) == my_list


if is_sorted(num_list):
    print("the list is sorted")
else:
    print("the list is not sorted")
