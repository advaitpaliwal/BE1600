def substitutionDecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    return plainText


testKey1 = "zyxwvutsrqponmlkjihgfedcba "
cipherText = 'gsv jfrxp yildm ulc'
print("CipherText:", cipherText)
print("PlainText:", substitutionDecrypt(cipherText, testKey1))
