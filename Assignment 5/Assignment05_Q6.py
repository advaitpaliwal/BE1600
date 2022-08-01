print("\nfirst nested loop")
for i in range(8):
    for j in range(i):
        print('*', end=" ")
    print()
print("\nsecond nested loop\n")
for i in range(7, 0, -1):
    for j in range(i):
        print('*', end=" ")
    print()
