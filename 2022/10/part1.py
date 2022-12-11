#!/usr/local/bin/python3

def get_signal(cycle,x):

    if cycle == 20 or (60 <= cycle <= 220 and (cycle-20)%40 == 0):
        return cycle * x

    return 0

def aoc():
    commands = []
    cycle = 0
    x = 1
    signal_total = 0

    with open("./input.txt") as infile:
        line = infile.readline().strip().split()
        while line:
            command = [line[0], 0] if line[0] == "noop" else [line[0], int(line[1])]
            commands.append(command)
            line = infile.readline().strip().split()

    for command in commands:
        if command[0] == "noop":
            cycle += 1
            signal_total += get_signal(cycle,x)
        else:
            cycle += 1
            signal_total += get_signal(cycle,x)
            cycle += 1
            signal_total += get_signal(cycle,x)
            x += command[1]

    print("Signal total: ", signal_total)

if __name__ == '__main__':
    aoc()
