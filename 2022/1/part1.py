#!/usr/local/bin/python3

def aoc():
    elf = 1
    elves = {}
    most_calories = 0

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
        if elves[k]["total"] > most_calories:
            most_calories = elves[k]["total"]

    print(most_calories)

if __name__ == '__main__':
  aoc()
