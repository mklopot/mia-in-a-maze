#!/usr/bin/python

import random
import sys
sys.setrecursionlimit(9999999)
width = 3
height = 3

grid = [[set(['up', 'down', 'left', 'right']) for j in range(width)] for i in range(height)] 
opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

print grid
start = (0,0)

def process_cell(cell):
    print "Function 'process_cell' called with", cell
    print "At cell: ",(cell)
    global grid
    print grid[cell[0]][cell[1]]
    dirs = (['up', 'down', 'left', 'right'])
    random.shuffle(dirs)
    nextcell = [0,0]
    for direction in dirs:
        print "Trying to go " + direction
        if direction == 'up':
            nextcell[0] = cell[0]
            nextcell[1] = cell[1] + 1
        elif direction == 'down':
            nextcell[0] = cell[0]
            nextcell[1] = cell[1] - 1
        elif direction == 'left':
            nextcell[1] = cell[1]
            nextcell[0] = cell[0] - 1
        elif direction == 'right':
            nextcell[1] = cell[1]
            nextcell[0] = cell[0] + 1
        
        if (0 <= nextcell[0] <= (height -1)) and (0 <= nextcell[1] <= (width -1)):
            print "Destination within bounds:",(nextcell)
            print grid[nextcell[0]][nextcell[1]]
            if (grid[nextcell[0]][nextcell[1]] == set(["up", "down", "left", "right"])):
                nextgridcell = grid[nextcell[0]][nextcell[1]]
                gridcell = grid[cell[0]][cell[1]]
                print "carving: " + direction + " wall from "+str(cell)
                gridcell.difference_update(set([direction]))
                print "carving: " + opposite[direction] + " wall from "+str(cell)
                nextgridcell.difference_update(set([opposite[direction]]))
                print "Carved:", gridcell 
                process_cell(nextcell)
            else:
                print "Cell ", nextcell, " already visited, going back..." 
        else:
            print "Destination out of bounds: ", nextcell

process_cell(start)
print grid

