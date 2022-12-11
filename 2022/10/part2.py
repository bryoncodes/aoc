#!/usr/local/bin/python3

def drawpixel(x,cycle):
    if cycle == 0:
        cycle = 40

    cycle -= 1
    if cycle >= x-1 and cycle <= x+1:
        return "#"

    return " "

def aoc():
    commands = []
    cycle = 0
    x = 1

    with open("./input.txt") as infile:
        line = infile.readline().strip().split()
        while line:
            command = [line[0], 0] if line[0] == "noop" else [line[0], int(line[1])]
            commands.append(command)
            line = infile.readline().strip().split()

    for command in commands:
        if command[0] == "noop":
            cycle += 1
            modcycle = cycle % 40
            if modcycle > 0:
                print(drawpixel(x,modcycle),end="")
            else:
                print(drawpixel(x,modcycle))
        else:
            cycle += 1
            modcycle = cycle % 40
            if modcycle > 0:
                print(drawpixel(x,modcycle),end="")
            else:
                print(drawpixel(x,modcycle))

            cycle += 1
            modcycle = cycle % 40
            if modcycle > 0:
                print(drawpixel(x,modcycle),end="")
            else:
                print(drawpixel(x,modcycle))

            x += command[1]

if __name__ == '__main__':
    aoc()
