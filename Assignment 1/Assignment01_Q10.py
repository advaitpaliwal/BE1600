def burned(cal_per_min, minutes):
    cal_burned = minutes * cal_per_min
    return cal_burned


print("Minutes   Calories Burned")
print("-------------------------")
for i in range(10, 35, 5):
    cal_burned = burned(3.9, i)
    print(f"{i}               {cal_burned}")
