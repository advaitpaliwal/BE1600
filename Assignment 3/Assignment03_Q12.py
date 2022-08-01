string_input = str(input("")).replace(" ", "")
unique_list = list(set(string_input))
l = [string_input.count(i) for i in unique_list]
count_dict = dict(zip(unique_list, l))
for key, value in sorted(count_dict.items()):
    print(f"{key.upper()} {'* '*value}")
