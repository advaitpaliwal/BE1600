def f_to_c():
    f_temp = -10.00
    with open("tempConv.txt", "w") as f:
        f.write("Fahrenhiet  Celsius\n")
        while f_temp < 11.00:
            c_temp = (f_temp - 32) * 5 / 9
            f.write("{:.2f}\t\t\t{:.2f}\n".format(f_temp, c_temp))
            f_temp += 1.00


f_to_c()
