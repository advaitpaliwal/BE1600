people = {}


def load():
    with open("people.txt", "r") as f:  # using with open to automatically close
        for element in f.readlines():  # readlines to provide a list
            name = element.split("\n")[0].split(",")[0]
            email = element.split("\n")[0].split(",")[1]
            people[name] = email


def lookup(name):
    return name in people.keys()  # returns bool if name is or is not in the keys


def unload():
    with open("people.txt", "w") as f:
        for key, value in people.items():
            # writes the entire dictionary in the file
            f.write(f"{key},{value}\n")


def menu():
    print("\nMenu\n----------------------------------------\n1. Look up an email address\n2. Add a new name and email address\n3. Change an existing email address\n4. Delete a name and email address\n5. Quit the program")


def main():
    load()  # loads dictionary of people
    invalid_selected = False
    menu()  # prints menu
    while True:
        if not invalid_selected:
            my_input = input("\nEnter your choice: ")
        else:
            my_input = input("\nPlease enter a valid option: ")

        if my_input == "1":
            name_input = input("Enter a name: ")
            if not lookup(name_input):
                print("The specified name was not found")
            else:
                print(f"Name: {name_input}\nEmail: {people[name_input]}")
        elif my_input == "2":
            name_input = input("Enter name: ")
            email_input = input("Enter email address: ")
            if lookup(name_input):
                print("That name already exists")
            else:
                people[name_input] = email_input
                print("Name and address have been added")
        elif my_input == "3":
            name_input = input("Enter name: ")
            email_input = input("Enter the new address: ")
            if not lookup(name_input):
                print("The specified name was not found")
            else:
                people[name_input] = email_input
                print("Information updated")
        elif my_input == "4":
            name_input = input("Enter name: ")
            if not lookup(name_input):
                print("The specified name was not found")
            else:
                del(people[name_input])
                print("Information deleted")
        elif my_input == "5":
            print("Information saved")
            break
        else:
            invalid_selected = True
            continue
        unload()  # writes items in people.txt if input is valid
        menu()


main()
