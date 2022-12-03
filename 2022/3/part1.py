#!/usr/local/bin/python3

def find_duplicate(sacks):
    compartment1 = sacks[:int(len(sacks)/2)]
    compartment2 = sacks[int(len(sacks)/2):]
    for i in compartment1:
        if i in compartment2:
            return i

def get_priority(item):
    priority = ord(item) - 96 if item == item.lower() else ord(item) - 64 + 26
    return priority

def rucksacks():
    total_priority = 0
    with open("./input") as infile:
        sacks = infile.readline().strip()
        while sacks:
            duplicate = find_duplicate(sacks)
            total_priority += get_priority(duplicate)
            sacks = infile.readline().strip()

    return total_priority

if __name__ == '__main__':
    print(rucksacks())
