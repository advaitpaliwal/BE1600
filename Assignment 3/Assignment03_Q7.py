string_input = str(input("Enter a string: ")).replace(" ", "")
unique_list = list(set(string_input))
l = [string_input.count(i) for i in unique_list]
print(
    f"The character that appears most frequently in the string is {unique_list[l.index(max(l))]}")
