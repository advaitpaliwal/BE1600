l = ["how", "are", "you?"]
extend_list = []


def two_list(my_list):
    for word in my_list:
        extend_list.extend([word] * 2)
    return extend_list


print(f"Original list: {l}")
print(f"Double list: {two_list(l)}")
