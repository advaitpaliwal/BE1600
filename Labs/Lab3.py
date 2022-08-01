def dist_trav(speed, hours):
    sum = 0
    for i in range(1, hours + 1):
        distance = i * speed
        sum = distance + sum
        print(f"{i}               {distance}")
    print(f"The accumalated distance travaled is: {sum}")


speed_inp = float(input("Enter the speed of the vehicle in mph: "))
hr_inp = int(input("Enter the number of hours traveled: "))


print("Hours   Distance Traveled")
print("-------------------------")
dist_trav(speed_inp, hr_inp)
