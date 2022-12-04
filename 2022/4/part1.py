#!/usr/local/bin/python3

def range_compare(sections):
    section1 = set()
    section2 = set()

    s1 = sections[0].split("-")
    s2 = sections[1].split
    
    for i in range(int(s1[0]),int(s1[1])+1):
        section1.add(i)

    for i in range(int(s2[0]),int(s2[1])+1):
        section2.add(i)

    if section1.issuperset(section2) or section2.issuperset(section1):
        return 1

    return 0

def camp_cleanup():
    pairs = 0
    with open("./input") as infile:
        sections = infile.readline().strip().split(",")
        while sections[0]:
            pairs += range_compare(sections)
            sections = infile.readline().strip().split(",")

    print(pairs)

if __name__ == '__main__':
    camp_cleanup()
