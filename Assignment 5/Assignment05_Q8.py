years = int(input("Enter the number of years: "))
months = 12
data = []
total_months = months * years
total = 0
for i in range(years):
    data.append([0] * months)
    print(f"For year {i+1} : ")
    for j in range(months):
        num_input = float(
            input(f"Enter the rainfall amount for the month {j+1}: "))
        data[i][j] = num_input
        total += num_input
print(f"For {total_months}")
print(f"Total rainfall: {total} inches")
print(f"Average monthly rainfall: {total/total_months} inches")
