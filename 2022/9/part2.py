#!/usr/local/bin/python3

visited = {}

def move_tail(head,tail):
    if head["x"] == tail["x"]:
        if head["y"] > tail["y"] and head["y"] - tail["y"] == 2:
            tail["y"] += 1
        if head["y"] < tail["y"] and tail["y"] - head["y"] == 2:
            tail["y"] -= 1

    if head["y"] == tail["y"]:
        if head["x"] > tail["x"] and head["x"] - tail["x"] == 2:
            tail["x"] += 1
        if head["x"] < tail["x"] and tail["x"] - head["x"] == 2:
            tail["x"] -= 1

    if head["x"] > tail["x"] and head["x"] - tail["x"] == 2:
        tail["x"] += 1
        if head["y"] < tail["y"]:
            tail["y"] -= 1
        if head["y"] > tail["y"]:
            tail["y"] += 1

    if head["x"] < tail["x"] and tail["x"] - head["x"] == 2:
        tail["x"] -= 1
        if head["y"] > tail["y"]:
            tail["y"] += 1
        if head["y"] < tail["y"]:
            tail["y"] -= 1

    if head["y"] > tail["y"] and head["y"] - tail["y"] == 2:
        tail["y"] += 1
        if head["x"] > tail["x"]:
            tail["x"] += 1
        if head["x"] < tail["x"]:
            tail["x"] -= 1

    if head["y"] < tail["y"] and tail["y"] - head["y"] == 2:
        tail["y"] -= 1
        if head["x"] > tail["x"]:
            tail["x"] += 1
        if head["x"] < tail["x"]:
            tail["x"] -= 1

    return tail

def process_move(head, tails, move):
    #move head
    if move == "R":
        head["x"] += 1
    if move == "L":
        head["x"] -= 1
    if move == "U":
        head["y"] += 1
    if move == "D":
        head["y"] -= 1

    #move tails, if needed
    tails[0] = move_tail(head,tails[0])
    for i in range(1,len(tails)):
        tails[i] = move_tail(tails[i-1],tails[i])

    #update record of visited spaces
    if tails[-1]["x"] in visited:
        visited[tails[-1]["x"]].append(tails[-1]["y"])
    else:
        visited[tails[-1]["x"]] = [tails[-1]["y"]]

    return (head,tails)

def aoc():
    moves = []
    with open("./input.txt") as infile:
        line = infile.readline().strip().split()
        while line:
            moves.append(line)
            line = infile.readline().strip().split()

    num_visited = 0
    head = {
        "x" : 0,
        "y" : 0
    }
    tails = []
    for i in range(9):
        tails.append({"x" : 0, "y" : 0})

    for i in range(len(moves)):
        #Move the head
        for j in range(int(moves[i][1])):
            (head,tails) = process_move(head,tails,moves[i][0])
            print(head)
            for k in range(len(tails)):
                print(tails[k])
            print("=====")

    for i in visited:
        for j in set(visited[i]):
            num_visited += 1

    return num_visited

if __name__ == '__main__':
    print(aoc())
