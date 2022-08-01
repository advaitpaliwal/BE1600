dict1 = {'a': 15, 'c': 35, 'b': 10}
print("Keys:", " ".join(map(str, dict1.keys())))
print("Values:", " ".join(map(str, dict1.values())))
print("Key-Value pairs")
for k, v in dict1.items():
    print(k, v)
print("Key-Value pairs- sorted by key")
for k, v in sorted(dict1.items()):
    print(k, v)
print("Key-Value pairs- sorted by value")
dict2 = dict(zip(dict1.values(), dict1.keys()))
for k, v in sorted(dict2.items()):
    print(v, k)
