#!/usr/local/bin/python3

def find_exits(grid,row,col):
    cur = 'a' if grid[row][col] == 'S' else grid[row][col]
    exits = {}
#    #print("Find exits for: ")
#    #print("Row: ",row)
#    #print("Col: ",col)
#    #print("Visited: ",visited)

    #check north
    if row > 0:
        exits.update({(row-1,col):{'weight':1}}) if ord(grid[row-1][col]) <= ord(cur) + 1 else exits.update({(row-1,col):{'weight':0}})
    #check south
    if row < len(grid)-1:
        exits.update({(row+1,col):{'weight':1}}) if ord(grid[row+1][col]) <= ord(cur) + 1 else exits.update({(row+1,col):{'weight':0}})
    #check east
    if col < len(grid[row])-1:
        exits.update({(row,col+1):{'weight':1}}) if ord(grid[row][col+1]) <= ord(cur) + 1 else exits.update({(row,col+1):{'weight':0}})
    #check west
    if col > 0 and (row,col-1):
        exits.update({(row,col-1):{'weight':1}}) if ord(grid[row][col-1]) <= ord(cur) + 1 else exits.update({(row,col-1):{'weight':0}})

#    #print("Exits: ",exits)
#    #print("=========")
#    #print("")
    
    return exits


def get_steps(map, coords, visited = []):
    print("Get steps: ")
    print("Map for ",coords, ": ", map[coords])
    print("Visited: ",visited)


    if map[coords]['value'] == 'E':
        return 1
    else:
        visited.append((coords))

        print("Visited: ",visited)
        print("=========")
        print("")

        if not map[coords]['exits']:
            if visited:
                del visited[-1]
            return -1

        count = -1

        for exit in map[coords]['exits']:
            #input()
            if exit not in visited and map[coords]['exits'][exit]['weight'] > 0:
                map[coords]['exits'][exit].update({'count': get_steps(map,exit,visited)})
            else:
                map[coords]['exits'][exit].update({'count': -1})
            
            print(map[coords]['exits'])
            print(exit)    
            
            if count < 0 or 0 < map[coords]['exits'][exit]['count'] < count:
                count = map[coords]['exits'][exit]['count']


        if visited:
            del visited[-1]

    return count + 1

def aoc():
    grid = []
    map = {}

    with open("./input2.txt") as infile:
        line = infile.readline().strip()
        while line:
            grid.append([letter for letter in line])
            line = infile.readline().strip()

    #build nodes & exits
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            map.update({(row,col):{'value':grid[row][col],"exits":find_exits(grid,row, col)}})
            if grid[row][col] == 'S':
                start = (row,col)



    answer =  get_steps(map, start)

    for i in map:
        print(i,":")
        for j in map[i]:
            print("  ",j,": ", map[i][j])
        print()

    return answer


if __name__ == '__main__':
    print(aoc())
    
