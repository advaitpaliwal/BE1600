with open("thisFile.txt", "r") as r:
    all_lines = r.read().split("\n")

with open("thatFile.txt", "w") as w:
    for line in all_lines:
        if all_lines.index(line) % 2 == 0:
            w.write(line + "\n")
