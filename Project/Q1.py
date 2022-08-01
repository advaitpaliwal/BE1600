
morse_code = {}
morse_code_rev = {}


def load():
    with open("morse.txt", "r") as f:  # using with open to automatically close the file
        for element in f.readlines():  # readlines gives a list of all lines
            eng = element.split("\n")[0].split(
                " ")[0]  # finding the english letter
            mors = element.split("\n")[0].split(
                " ")[1]  # finding the morse equivalent
            # loading a dictionary with english letters as key
            morse_code[eng] = mors
            # loading a dictionary with morse letters as key
            morse_code_rev[mors] = eng


def mors_encode(input_text):
    # adds a space between each character to make morse easier to read
    input_text = " ".join(list(input_text.upper()))
    for ch in input_text:
        if ch in str(morse_code) and ch != " ":
            # replacing every english with morse in the same word
            input_text = input_text.replace(ch, morse_code[ch])
    return input_text


def mors_decode(input_text):
    # replacing all triple spaces with double and splitting single space to
    # get a regular sentence
    input_text = input_text.replace("   ", "  ").split(" ")
    for ch in input_text:
        if ch in str(morse_code_rev) and ch != " " and ch != "":
            # replacing items in the list using indexing
            input_text[input_text.index(ch)] = morse_code_rev[ch]
        if ch == "":
            input_text[input_text.index(ch)] = " "
    return "".join(input_text)  # joining items


def menu():
    print("\nHello, this program allows you to translate text to morse code or translate morse code to text.")
    print("\nPlease, select one of the below options:")
    print("\n*** Enter 't' for encoding text\n*** Enter 'm' for decoding morse code\n*** Enter 'e' to exit the program.")


def main():
    invalid_selected = False
    menu()  # prints menu
    load()  # loads translation
    while True:
        if not invalid_selected:
            my_input = input("My input is: ")
        else:
            my_input = input("Please enter a valid option: ")
        if my_input == "t":
            input_text = input("\nPlease enter text to translate:\n")
            print(mors_encode(input_text))
        elif my_input == "m":
            input_text = input("\nPlease enter morse to translate:\n")
            print(mors_decode(input_text))
        elif my_input == "e":
            print("\nThanks for using this program!")
            break
        else:
            print("***invalid option.")
            invalid_selected = True
            continue  # continues if invalid selected
        menu()  # loads menu after successful translation


main()
