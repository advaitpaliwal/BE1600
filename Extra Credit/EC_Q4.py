import csv


def find_max(my_list):
    max = 0
    for x in my_list:
        if x > max and x > 0:
            max = x
    return max


def find_min(my_list):
    min = 999999
    for x in my_list:
        if x < min and x > 0:
            min = x
    return min


with open("best_and_worst.txt", 'a') as f:
    f.write("Indicator\t\t\t\t\t\t\t\t: Min\t\t\t\t\t\t\tMax")
    f.write("\n----------------------------------------------------------------------------------------------------")
    with open("riskfactors.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in range(5):
            next(csv_reader)
        lines = [line for line in csv_reader]
        states = []
        for j in range(1, len(lines[0])):
            data = []
            for i in range(1, len(lines)):
                x = lines[i][j]
                if "%" in x:
                    x = x.replace('%', '')
                if x == "N/A":
                    x = x.replace("N/A", "-1")
                data.append(float(x))
                states.append(lines[i][0])
            max_value = find_max(data)
            max_inx = data.index(max_value)
            max_state = states[max_inx]
            min_value = find_min(data)
            min_inx = data.index(min_value)
            min_state = states[min_inx]
            rate_type = lines[0][j]
            f.write("\n{:40s}: {:21s} {:6.1f}\t{:21s} {:6.1f}".format(
                rate_type, min_state, min_value, max_state, max_value))
