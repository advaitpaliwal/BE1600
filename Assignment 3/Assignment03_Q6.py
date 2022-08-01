num_list = []
for i in range(10):
    input_num = float(input("Enter a number: "))
    num_list.append(input_num)
print(f"Low: {min(num_list)}")
print(f"High: {max(num_list)}")
print(f"Total: {sum(num_list)}")
print(f"Average: {sum(num_list)/len(num_list)}")
