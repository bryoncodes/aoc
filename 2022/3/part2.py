#!/usr/local/bin/python3

def find_badge(sacks):
    for i in sacks[0]:
        if i in sacks[1]:
            if i in sacks[2]:
                return i

def get_priority(item):
    priority = ord(item) - 96 if item == item.lower() else ord(item) - 64 + 26
    return priority

def rucksacks():
    total_priority = 0
    sacks = ['','','']
    with open("./input") as infile:
        sacks[0] = infile.readline().strip()
        sacks[1] = infile.readline().strip()
        sacks[2] = infile.readline().strip()
        while sacks[2]:
            badge = find_badge(sacks)
            total_priority += get_priority(badge)
            sacks[0] = infile.readline().strip()
            sacks[1] = infile.readline().strip()
            sacks[2] = infile.readline().strip()

    return total_priority

if __name__ == '__main__':
    print(rucksacks())
