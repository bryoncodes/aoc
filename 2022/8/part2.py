#!/usr/local/bin/python3

def check_visibility(trees,row,col,rows,cols):
    up=down=left=right=0

    #up
    if row == 0:
        pass
    else:
        for i in range(row-1,-1,-1):
            if trees[i][col] < trees[row][col]:
                up += 1
            else:
                up += 1
                break

    #down
    if row == rows -1:
        pass
    else:
        for i in range(row+1,rows):
            if trees[i][col] < trees[row][col]:
                down += 1
            else:
                down += 1
                break

    #left
    if col == 0:
        pass
    else:
        for i in range(col-1,-1,-1):
            if trees[row][i] < trees[row][col]:
                left += 1
            else:
                left += 1
                break

    #right
    if col == cols -1:
        pass
    else:
        for i in range(col+1,cols):
            if trees[row][i] < trees[row][col]:
                right += 1
            else:
                right += 1
                break

    return(up * down * left * right)

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
    best_view = 0
    trees = build_tree_array()
    rows = len(trees)
    cols = len(trees[0])

    for row in range(rows):
        for col in range(cols):
            view = check_visibility(trees, row , col, rows, cols)
            if view > best_view:
                best_view = view
    return best_view

if __name__ == '__main__':
    print(aoc())
