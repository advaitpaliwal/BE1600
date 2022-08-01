original_list = [
    'be',
    'be',
    'is',
    'not',
    'or',
    'question',
    'that',
    'the',
    'to',
    'to']


def remove_duplicates(my_list):
    return sorted(list(set(my_list)))


print(f"Original list: {original_list}")
print(f"List after removing duplicates: {remove_duplicates(original_list)}")
