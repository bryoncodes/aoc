#!/usr/local/bin/python3

visited = {}

def process_move(head, tail, move):
    #move head
    if move == "R":
        head["y"] += 1
    if move == "L":
        head["y"] -= 1
    if move == "U":
        head["x"] -= 1
    if move == "D":
        head["x"] += 1

    #move tail, if needed
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
        if head["y"] != tail["y"]:
            tail["y"] = head["y"]

    if head["x"] < tail["x"] and tail["x"] - head["x"] == 2:
        tail["x"] -= 1
        if head["y"] != tail["y"]:
            tail["y"] = head["y"]

    if head["y"] > tail["y"] and head["y"] - tail["y"] == 2:
        tail["y"] += 1
        if head["x"] != tail["x"]:
            tail["x"] = head["x"]

    if head["y"] < tail["y"] and tail["y"] - head["y"] == 2:
        tail["y"] -= 1
        if head["x"] != tail["x"]:
            tail["x"] = head["x"]

    if tail["x"] in visited:
        visited[tail["x"]].append(tail["y"])
    else:
        visited[tail["x"]] = [tail["y"]]

    return (head,tail)

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
    tail = {
        "x" : 0,
        "y" : 0
    }

    for i in range(len(moves)):
        #Move the head
        for j in range(int(moves[i][1])):
            (head,tail) = process_move(head,tail,moves[i][0])

    for i in visited:
        for j in set(visited[i]):
            num_visited += 1

    return num_visited

if __name__ == '__main__':
    print(aoc())
