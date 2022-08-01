rows = 4
columns = 3
alpha = []
for i in range(rows):
    alpha.append([0] * columns)
print("part a")
for i in range(rows):
    for j in range(columns):
        print(alpha[i][j], end=" ")
    print("")
print("part b")
for i in range(rows):
    if i == 0:
        alpha[i] = [1] * columns
    else:
        alpha[i] = [3] * columns
for i in range(rows):
    for j in range(columns):
        print(alpha[i][j], end=" ")
    print("")
print("part c")
for i in range(rows):
    alpha[i][0] = 2
    alpha[i][1] = alpha[i][0] * 2
    alpha[i][2] = alpha[i][1] * 2
for i in range(rows):
    for j in range(columns):
        print(alpha[i][j], end=" ")
    print("")
