def repeat(word, times):
    final = ""
    for _ in range(times):
        final = final + word
    return final


word = str(input("What word would you like to repeat? "))
times = int(input("How many times would you like to repeat? "))

result = repeat(word, times)
print(result)
