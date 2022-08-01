def getData():
    data = []
    for i in range(2):
        data.append([0] * 12)
    print("Enter highest temperatures for each month of the year.")
    for i in range(12):
        data[0][i] = int(input(f"Month {i+1}: "))
    print("Enter lowest temperatures for each month of the year.")
    for i in range(12):
        data[1][i] = int(input(f"Month {i+1}: "))
    return data


data = getData()


def averageHigh():
    return sum(data[0]) / 12


def averageLow():
    return sum(data[1]) / 12


def highTemp():
    return max(data[0])


def lowTemp():
    return min(data[1])


print("List of the highest and lowest temperatures for each month of the year")
for i in range(2):
    for j in range(12):
        print(data[i][j], end=" ")
    print()
print(f"Average high temperature for the year {averageHigh()}")
print(f"Average low temperature for the year {averageLow()}")
print(f"Highest high temperature for the year {highTemp()}")
print(f"Lowest low temperature for the year {lowTemp()}")
