with open("Labs/numbers.txt", "r") as f:
    numbers_list = [int(line.split("\n")[0].split(" ")[1])
                    for line in f.readlines()]
    evens = len([num for num in numbers_list if num % 2 == 0])
    print(f"""
    count = {len(numbers_list)}
    sum = {sum(numbers_list)}
    evens = {evens}
    average = {sum(numbers_list)/len(numbers_list)}
    """
          )
