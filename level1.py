#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

import framework
import mia
import doomimp
import brick
import maze

def level():
    global player
    player = mia.Mia(x=300,y=450)
    framework.space.add(player.body)
    for shape in player.shapes:
        framework.space.add(shape)
    player.add(framework.characters)    

    npcs = [doomimp.DoomImp(x=200, y=250, target=player), doomimp.DoomImp(x=600, y=150, target=player), doomimp.DoomImp(x=550,y=560,target=player)]
    for npc in npcs:
        framework.space.add(npc.body)
        for shape in npc.shapes:
            framework.space.add(shape)
        npc.add(framework.characters)
            
    bricks = []
    #for i in range(1,12):
    #    bricks.append(brick.Brick(size=40, y=45*i))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=150, x=100+21*i))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=250, x=100+21*i))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=350, x=100+21*i))
    
    for brickinstance in bricks:    
        framework.primitives.append(brickinstance)
        framework.space.add(brickinstance.body)
        framework.space.add(brickinstance.shape)    
    
    staticbricks = []
    staticbricks.append(brick.StaticBrick(x=425, y=50, width=50, height=10))
    staticbricks.append(brick.StaticBrick(x=350, y=270, width=10, height=420))
    staticbricks.append(brick.StaticBrick(x=370, y=620, width=800, height=10))
    for staticbrick in staticbricks:
        framework.primitives.append(staticbrick)
        framework.space.add(staticbrick.shape)
    
    maze.make_maze(100, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)    

    maze.make_maze(540, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)

    maze.make_maze(840, 80, width=40, height=10, cellwidth=90, cellheight=65, wallthickness=20)
    
    
    framework.prize = (brick.Polygon(radius=15, num_pts=6, x=300, y=500))
    framework.prize.shape.layers = 0b1000
    framework.primitives.append(framework.prize)
    framework.space.add(framework.prize.body)
    framework.space.add(framework.prize.shape)

#    joint = pymunk.SlideJoint(player.body, prize.body, (0,0), (0,0), min=20, max=27)
#    framework.space.add(joint)
