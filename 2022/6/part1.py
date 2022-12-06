#!/usr/local/bin/python3

def aoc():

    with open("./input.txt") as infile:
        line = infile.readline().strip("\n")

    inputlength = len(line)
    for i in range(inputlength):
        if i <= inputlength - 4:
            sample = line[i:i+4]
            sampleset = set()
            for j in sample:
                sampleset.add(j)
            if len(sampleset) == 4:
                return(i+4)

if __name__ == '__main__':
    print(aoc())
