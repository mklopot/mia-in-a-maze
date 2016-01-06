#!/usr/bin/python

import random
import sys

import framework
import brick

if framework.debug:
    def dprint(*output):
        print(output)
else:
    def dprint(*output):
        pass

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
    
    return grid


def process_cell(cell):
    """Processes the maze one cell at a time, carving out walls, moving to neighboring cells, and recursively calling itself"""
    global opposite
    dprint("Function 'process_cell' called with", cell)
    dprint("At cell: ",(cell))
    global grid
    dprint(grid[cell[0]][cell[1]])
    directions = (['up', 'down', 'left', 'right'])
    random.shuffle(directions)
    nextcell = list(cell)
    for direction in directions:
        dprint("Trying to go " + direction)
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
            dprint("Destination within bounds:",(nextcell))
            
            nextgridcell = grid[nextcell[0]][nextcell[1]]
            dprint(nextgridcell)
            if (nextgridcell == set(["up", "down", "left", "right"])):
                gridcell = grid[cell[0]][cell[1]]
                dprint("carving: " + direction + " wall from "+str(cell))
                gridcell.difference_update(set([direction]))
                dprint("carving: " + opposite[direction] + " wall from "+str(cell))
                nextgridcell.difference_update(set([opposite[direction]]))
                dprint("Carved:", gridcell) 
                process_cell(nextcell)
            else:
                pass
                dprint("Cell ", nextcell, " already visited, going back..." )
        else:
            pass
            dprint("Destination out of bounds: ", nextcell)

 
def make_maze(x, y, width, height, cellwidth, cellheight, wallthickness):

    mazegrid = make_grid(width, height)
    mazebricks = []
    for i in range(height):
        for j in range (width):
            if 'up' in mazegrid[i][j]:
                downbrick = brick.StaticBrick(cellwidth, wallthickness, x + i * cellwidth, y + j * cellheight + cellheight/2)
                downbrick.shape.group = 1
                framework.space.add(downbrick.shape)
                framework.primitives.append(downbrick)
            elif j % 2 == 1:
                downbrick = brick.StaticBrick(wallthickness*2, wallthickness, x + i * cellwidth - cellwidth/2 + wallthickness, y + j * cellheight + cellheight/2)
                downbrick.shape.group = 1
                framework.space.add(downbrick.shape)
                framework.primitives.append(downbrick)
            else:
                downbrick = brick.StaticBrick(wallthickness*2, wallthickness, x + i * cellwidth + cellwidth/2 - wallthickness, y + j * cellheight + cellheight/2)
                downbrick.shape.group = 1
                framework.space.add(downbrick.shape)
                framework.primitives.append(downbrick)
                
            if 'left' in mazegrid[i][j]:
                leftbrick = brick.StaticBrick(wallthickness, cellheight - wallthickness, x + i * cellwidth - cellwidth/2, y + j * cellheight)
                leftbrick.shape.group = 1
                framework.space.add(leftbrick.shape)
                framework.primitives.append(leftbrick)
            
    
if __name__ == "__main__":
    make_grid(20,30)
