def word_count(word):
    count = len(word.split())
    return count


word = str(input("Type the sentence below and I will count the words.\n"))
count = word_count(word)
print(f"'{word}' -> {count}")
