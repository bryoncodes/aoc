#!/usr/bin/python

def aoc():
    total=0
    with open("./input") as infile:
        line = infile.readline()
        while line:
            mass = int(line.strip())
            fuel = (mass / 3) - 2
            total += fuel
            line = infile.readline()
        print total

if __name__ == '__main__':
    aoc()
