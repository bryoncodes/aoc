#!/usr/local/bin/python3

def aoc():
    elf = 1
    elves = {}
    most_calories = {"elf" : 0, "calories" : 0}
    most_calories_2 = {"elf" : 0, "calories" : 0}
    most_calories_3 = {"elf" : 0, "calories" : 0}

    with open("./input") as infile:
        line = infile.readline()
        elves[elf] = {"calories" : []}

        while line:
            if line.strip():
                elves[elf]["calories"].append(int(line.strip()))
            else:
                elf += 1
                elves[elf] = {"calories" : []}
            line = infile.readline()

    for k in elves:
        elves[k]["total"] = sum(elves[k]["calories"])
        if elves[k]["total"] > most_calories["calories"]:
            most_calories["calories"] = elves[k]["total"]
            most_calories["elf"] = k

    for k in elves:
        if k != most_calories["elf"] and elves[k]["total"] > most_calories_2["calories"]:
            most_calories_2["calories"] = elves[k]["total"]
            most_calories_2["elf"] = k

    for k in elves:
        if k != most_calories["elf"] and k != most_calories_2["elf"] and elves[k]["total"] > most_calories_3["calories"]:
            most_calories_3["calories"] = elves[k]["total"]
            most_calories_3["elf"] = k

    print(most_calories["calories"] + most_calories_2["calories"] + most_calories_3["calories"])

if __name__ == '__main__':
  aoc()
