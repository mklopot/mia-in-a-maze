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
            
    #left_border = pymunk.Segment(pymunk.Body(), (0,0), (0, 600), 5)
    #right_border = pymunk.Segment(pymunk.Body(), (800,0), (800, 600), 5)
    #top_border = pymunk.Segment(pymunk.Body(), (0,0), (800, 0), 5)
    bottom_border = pymunk.Segment(pymunk.Body(), (0,600), (800, 600), 5)
    #line = pymunk.Segment(pymunk.Body(), (50.0,500.0), (500.0, 500.0), 5)
    #line1 = pymunk.Segment(pymunk.Body(), (500.0,540.0), (550.0, 540.0), 5)
    #diag = pymunk.Segment(pymunk.Body(), (100.0,450.0), (450.0, 140.0), 5)
    #segments = [left_border, right_border, top_border, bottom_border, line, line1, diag]
    segments = [bottom_border]
    for segment in segments:
        segment.elasticity = 0
        segment.friction = .9
        segment.collision_type = 1
        framework.space.add(segment)
    
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
    #staticbricks.append(brick.StaticBrick(x=78, y=225, width=50, height=10))
    for staticbrick in staticbricks:
        framework.primitives.append(staticbrick)
        framework.space.add(staticbrick.shape)
    
    maze.make_maze(100, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)    

    maze.make_maze(540, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)
    
    
    prize = (brick.Star(inner_radius=5, outer_radius=20, num_pts=6, x=540, y=450))
    framework.primitives.append(prize)
    framework.space.add(prize.body)
    framework.space.add(prize.shape)

    joint = pymunk.SlideJoint(player.body, prize.body, (0,0), (0,0), min=20, max=27)
    framework.space.add(joint)
