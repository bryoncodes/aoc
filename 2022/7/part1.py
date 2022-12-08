#!/usr/local/bin/python3

def getsizes(dir, dirs):
    total = 0
    files = dirs[dir]
    for file in files:
        if file[0] == "dir":
            if dir == "/":
                total += getsizes("".join([dir,file[1]]), dirs)
            else:
                total += getsizes("/".join([dir,file[1]]), dirs)
        else:
            total += int(file[0])
    return total

def readfiles(i, input):
    files = []
    i += 1
    x = len(input)
    line = input[i].strip("\n").split()
    while line:
        if line[0] != "$":
            files.append(line)
            i += 1
            if i<x:
                line = input[i].strip("\n").split()
            else:
                line = []
        else:
            break
    return files

def buildtree(input):
    dirhistory = []
    dir = ""
    files = {}
    for i,line in enumerate(input):
        line = line.strip("\n").split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] != "..":
                    if line[2] == "/":
                        dirhistory = ["/"]
                        dir = "/"
                    else:
                        dirhistory.append(line[2])
                else:
                    dirhistory.pop()
            elif line[1] == "ls":
                path="/" + "/".join(dirhistory[1:])
                files[path] = readfiles(i, input)

    return files


def aoc():

    with open("./input.txt") as infile:
        input = infile.readlines()
    files = buildtree(input)
    total = 0
    for file in files:
        size = getsizes(file, files)
        if size <= 100000:
            total += size

    return total

if __name__ == '__main__':
    print(aoc())
