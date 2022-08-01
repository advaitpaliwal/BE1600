import string
file_input = str(input("enter file name "))
with open(file_input, "r") as r:
    all_lines = list(r.read().lower())
    occurances = {}
    for j in string.ascii_lowercase:
        occurances[j.lower()] = 0
    for i in all_lines:
        if i.lower() in string.ascii_lowercase:
            occurances[i.lower()] += 1
print("letter\tcount")
for k, v in sorted(occurances.items()):
    print(f"{k}\t{v}")
