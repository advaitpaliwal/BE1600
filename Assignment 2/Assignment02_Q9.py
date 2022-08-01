def num_vowel(word):
    num_v = 0
    num_c = 0
    vowels = "aeiou"
    word = word.lower()
    for letter in word:
        if letter in vowels:
            num_v += 1
        else:
            num_c += 1
    return num_v, num_c


str_input = input("Enter a string: ")
num_v, num_c = num_vowel(str_input)
print(f"The string you entered includes {num_v} vowels and {num_c} consonants")
