#!/usr/local/bin/python3

def load_monkeys(lines):
    #Build initial monkeys object
    monkey_count = 0
    monkey = {}
    monkeys = {}

    for line in lines:
        line = line.strip().split()
        if line == []:
            monkey['inspects'] = 0
            monkeys[monkey_count] = monkey
            monkey_count += 1
            monkey = {}
        elif line[0] == 'Starting':
            monkey['items'] = []
            tmp = line[2:]
            for i in range(len(tmp)):
                monkey['items'].append(int(tmp[i].strip(',')))
        elif line[0] == 'Operation:':
            monkey['op'] = line[4]
            monkey['val'] = line[5]
        elif line[0] == 'Test:':
            monkey['test'] = int(line[-1])
        elif line[1] == 'true:':
            monkey["true"] = line[-1]
        elif line[1] == 'false:':
            monkey["false"] = line[-1]
        else:
            pass

    #Add the final monkey to the dict
    monkey['inspects'] = 0
    monkeys[monkey_count] = monkey

    return monkeys

def aoc():
    with open("./input.txt") as infile:
        lines = infile.readlines()

    monkeys = load_monkeys(lines)

    mod = 1
    for m in monkeys:
        mod *= monkeys[m]['test']

    #Start processing 10000 rounds
    for round in range(10000):
        for monkey in range(len(monkeys)):
            while monkeys[monkey]['items'] != []:
                item = monkeys[monkey]['items'].pop(0)
                val = item if monkeys[monkey]['val'] == 'old' else int(monkeys[monkey]['val'])
                if monkeys[monkey]['op'] == '*':
                    item = item * val
                if monkeys[monkey]['op'] == '+':
                    item = item + val
                item = item % mod
                dest_monkey = monkeys[monkey]['true'] if item % monkeys[monkey]['test'] == 0 else monkeys[monkey]['false']
                monkeys[int(dest_monkey)]['items'].append(item)
                monkeys[monkey]['inspects'] += 1

    inspects = []
    for m in monkeys:
        inspects.append(monkeys[m]['inspects'])

    inspects.sort()
    return inspects.pop() * inspects.pop()


if __name__ == '__main__':
    print(aoc())
