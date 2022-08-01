import math


def distance(p1, p2):
    p1[0] = float(p1[0])
    p2[0] = float(p2[0])
    p1[1] = float(p1[1])
    p2[1] = float(p2[1])
    d = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d


l = []
with open("data.txt", "r") as f:
    for pair in f.readlines():
        l.append(pair.strip().split(" "))
rows = len(l)
columns = len(l[0])
print("    P1   P2   P3   P4   P5   P6   P7   P8")
for i in range(rows):
    p1 = l[i]
    print(f"P{i+1} ", end=" ")
    for j in range(rows):
        p2 = l[j]
        print(format(distance(p1, p2), ".2f"), end=" ")
    print()
