two_d = [[2, 3, 5], [-8, 4, 6], [9, 3, 77], [11, -2, 9]]
print("2D list")
for i in range(4):
    for j in range(3):
        print("{:3s}".format(str(two_d[i][j])), end=" ")
    print()


def output(my_list):
    row = 1
    for i in my_list:
        count = 0
        for x in i:
            if x >= 0 and x % 2 == 0:
                count += 1
        print(f"Row {row} : {count}")
        row += 1


print("\nNumber of even non negative values")
output(two_d)
