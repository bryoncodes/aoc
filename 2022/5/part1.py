#!/usr/local/bin/python3

def aoc():
    lines = []
    stacks = {}
    columns = []

    with open("./input") as infile:
        line = infile.readline().strip("\n")
        while line[1] != "1":
            lines.append(line)
            line = infile.readline().strip("\n")

        for i in range(len(line)):
            if line[i] != " ":
                columns.append(i)

        numstacks = int(line[-1])
        for i in range(0,numstacks):
            stacks[i+1] = []

            for j in lines[::-1]:
                if len(j) > columns[i]:
                    if j[columns[i]] != ' ':
                        stacks[i+1].append(j[columns[i]])

        line = infile.readline().strip("\n") #discard blank line
        line = infile.readline().strip("\n")
        while line:
            moves = line.split()
            for i in range(int(moves[1])):
                stacks[int(moves[5])].append(stacks[int(moves[3])].pop())
            line = infile.readline().strip("\n")

    top_crates=''
    for i in range(0,numstacks):
        top_crates += stacks[i+1][-1]

    print(top_crates)

if __name__ == '__main__':
    aoc()
