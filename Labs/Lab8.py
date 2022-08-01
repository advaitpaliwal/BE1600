my_dict = {
    'Kendrick': 'Perkins',
    'Stuart': 'Reges',
    'Jessica': 'Wolk',
    'Bruce': 'Reges',
    'Hal': 'Perkins'}
my_dict2 = {
    'Marty': 'Stepp',
    'Stuart': 'Reges',
    'Jessica': 'Wolk',
    'Allison': 'Obourn',
    'Hal': 'Perkins'}


def is_unique(dictionary):
    return sorted(list(dictionary.values())) == sorted(
        list(set(dictionary.values())))


print(is_unique(my_dict))
print(is_unique(my_dict2))
