with open("WorldSeries.txt", "r") as f:
    world_series = {}
    year = 1903
    teams = [line.strip().split("\n") for line in f.readlines()]
for team in teams:
    world_series[str(year)] = team[0]
    year += 1
while True:
    year_input = input("Enter a year in the range 1903-2020: ")
    try:
        print(
            f"The team that won the world series in {year_input} is the {world_series[year_input]}")
    except BaseException:
        print(f"The world series wasn't played in the year {year_input}")
    question = input("Do you want continue, type 'y' for Yes, 'n' for No ")
    if question == "n":
        break
