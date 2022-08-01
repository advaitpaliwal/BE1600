string_input = input(str("Enter a string "))


def vowel_replace(input):
    input = input.upper()
    vowels = "AEIOU"
    j = 0
    for i in input:
        if i in vowels:
            input = input.replace(i, "*")
            j += 1
    return input, j


string_output, num_vowel = vowel_replace(string_input)

print(f"Old String: {string_input}")
print(f"New String: {string_output}")
print(f"Number of vowel characters: {num_vowel}")
