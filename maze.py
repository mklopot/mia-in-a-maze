#!/usr/bin/python

import random
import sys
#sys.setrecursionlimit(9999999)

import framework
import brick

def make_grid(width, height, start=(0,0)):
    """Generates a random maze, returns an array of cells, each cell contains some walls"""
    
    global gridwidth
    gridwidth = width
    
    global gridheight
    gridheight = height
    
    global grid
    grid = [[set(['up', 'down', 'left', 'right']) for j in range(width)] for i in range(height)] 
    
    global opposite
    opposite = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}

    process_cell(start)
    
    print grid
    return grid


def process_cell(cell):
    """Processes the maze one cell at a time, carving out walls, moving to neighboring cells, and recursively calling itself"""
    global opposite
    print "Function 'process_cell' called with", cell
    print "At cell: ",(cell)
    global grid
    print grid[cell[0]][cell[1]]
    directions = (['up', 'down', 'left', 'right'])
    random.shuffle(directions)
    nextcell = list(cell)
    for direction in directions:
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
        
        global gridheight
        global gridwidth
        
        
        if (0 <= nextcell[0] <= (gridheight -1)) and (0 <= nextcell[1] <= (gridwidth -1)):
            print "Destination within bounds:",(nextcell)
            
            nextgridcell = grid[nextcell[0]][nextcell[1]]
            print nextgridcell
            if (nextgridcell == set(["up", "down", "left", "right"])):
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

 
def make_maze(x, y, width, height, cellwidth, cellheight, wallthickness):

    mazegrid = make_grid(width, height)
    mazebricks = []
    for i in range(height):
        for j in range (width):
            if 'up' in mazegrid[i][j]:
                downbrick = brick.StaticBrick(cellwidth, wallthickness, x + i * cellwidth, y + j * cellheight + cellheight/2)
                framework.space.add(downbrick.shape)
                framework.primitives.append(downbrick)
            if 'left' in mazegrid[i][j]:
                leftbrick = brick.StaticBrick(wallthickness, cellheight, x + i * cellwidth - cellwidth/2, y + j * cellheight)
                framework.space.add(leftbrick.shape)
                framework.primitives.append(leftbrick)
            
    
if __name__ == "__main__":
    make_grid(20,30)
