#!/usr/local/bin/python3

def aoc():

    with open("./input.txt") as infile:
        line = infile.readline().strip("\n")

    inputlength = len(line)
    for i in range(inputlength):
        if i <= inputlength - 14:
            sample = line[i:i+14]
            sampleset = set()
            for j in sample:
                sampleset.add(j)
            if len(sampleset) == 14:
                return(i+14)

if __name__ == '__main__':
    print(aoc())
