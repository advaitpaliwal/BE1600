def encrypt(word):
    cipher = ""
    start = 2
    while start > -1:
        for i in range(start, len(word), 3):
            cipher = cipher + word[i]
        start -= 1
    return cipher


plain_txt = str(input("PlainText: "))
print("CipherText", encrypt(plain_txt.upper()))
