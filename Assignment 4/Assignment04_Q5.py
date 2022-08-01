with open("books.txt", "r") as r:
    all_lines = r.read().split("\n")
    all_lines.remove("")
    authors = [line.strip().split(",")[1] for line in all_lines]
    books = [line.strip().split(",")[0] for line in all_lines]
    my_dict = {}
    for author in authors:
        if author in my_dict:
            my_dict[author].append(books[authors.index(author)])
        else:
            my_dict[author] = [books[authors.index(author)]]

for key, value in my_dict.items():
    print(key, value)
