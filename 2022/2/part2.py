#!/usr/local/bin/python3

def get_score(round):
    score = 0
    if round[1] == 'X':
        if round[0] == 'A':
            score += 3
        if round[0] == 'B':
            score += 1
        if round[0] == 'C':
            score += 2
    if round[1] == 'Y':
        score += 3
        if round[0] == 'A':
            score += 1
        if round[0] == 'B':
            score += 2
        if round[0] == 'C':
            score += 3
    if round[1] == 'Z':
        score += 6
        if round[0] == 'A':
            score += 2
        if round[0] == 'B':
            score += 3
        if round[0] == 'C':
            score += 1

    return score


def rps():
    total_score = 0
    with open("./input") as infile:
        round = infile.readline().split()
        while round:
            total_score += get_score(round)
            round = infile.readline().split()

    return total_score

if __name__ == '__main__':
    print(rps())
