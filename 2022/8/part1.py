#!/usr/local/bin/python3

def check_visibility(trees,row,col,rows,cols):
    visible = 1
    #All edge trees are visible
    if row == 0 or row == rows-1 or col == 0 or col == cols -1:
        pass
    else:
        #Check height of trees in column
        for i in range(row-1,-1,-1):
            if trees[i][col] >= trees[row][col]:
                visible = 0
        if visible:
            return 1

        visible = 1
        for i in range(row+1,rows):
            if trees[i][col] >= trees[row][col]:
                visible = 0
        if visible:
            return 1

        #Check height of trees in row
        visible = 1
        for i in range(col-1,-1,-1):
            if trees[row][i] >= trees[row][col]:
                visible = 0
        if visible:
            return 1

        visible = 1
        for i in range(col+1,cols):
            if trees[row][i] >= trees[row][col]:
                visible = 0
        if visible:
            return 1

    return visible

def build_tree_array():
    trees = []
    with open("./input.txt") as infile:
        line = infile.readline().strip()
        while line:
            row = []
            for i in range(len(line)):
                row.append(int(line[i]))
            trees.append(row)
            line = infile.readline().strip()

    return trees

def aoc():
    num_visible = 0
    trees = build_tree_array()
    rows = len(trees)
    cols = len(trees[0])

    for row in range(rows):
        for col in range(cols):
            num_visible += check_visibility(trees, row , col, rows, cols)
    return num_visible

if __name__ == '__main__':
    print(aoc())
