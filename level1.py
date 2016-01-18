#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

import framework
import mia
import cassie
import doomimp
import brick
import maze
import sprite
import airship

def level():
    global player
#    player = mia.Mia(x=300,y=450)
    player = mia.Mia(x=300,y=0)
    framework.space.add(player.body)
    for shape in player.shapes:
        framework.space.add(shape)
    player.add(framework.characters)    

    player2 = cassie.Cassie(x=600,y=0)
    framework.space.add(player2.body)
    for shape in player2.shapes:
        framework.space.add(shape)
    player2.add(framework.characters)    
    
    global playable
    playable = [player, player2]

    npcs = [doomimp.DoomImp(x=200, y=250, target=player), doomimp.DoomImp(x=600, y=150, target=player), doomimp.DoomImp(x=550,y=560,target=player)]
#    npcs = []
    for npc in npcs:
        framework.space.add(npc.body)
        for shape in npc.shapes:
            framework.space.add(shape)
        npc.add(framework.characters)
            
#    bricks = []
#    for i in range(1,8):
#        bricks.append(brick.Brick(size=40, x=85*i, y=-400))
#    for i in range(1,20):
#        bricks.append(brick.Brick(size=10, y=150, x=100+21*i))
#    for i in range(1,20):
#        bricks.append(brick.Brick(size=10, y=250, x=100+21*i))
#    for i in range(1,20):
#        bricks.append(brick.Brick(size=10, y=350, x=100+21*i))
#    
#    for brickinstance in bricks:    
#        framework.primitives.append(brickinstance)
#        framework.space.add(brickinstance.body)
#        framework.space.add(brickinstance.shape)    
    
    staticbricks = []
    staticbricks.append(brick.StaticBrick(x=425, y=50, width=50, height=10))
    staticbricks.append(brick.StaticBrick(x=350, y=270, width=10, height=420))
    staticbricks.append(brick.StaticBrick(x=370, y=640, width=800, height=10))
    for staticbrick in staticbricks:
        framework.primitives.append(staticbrick)
        framework.space.add(staticbrick.shape)
    
    maze.make_maze(100, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)    

    maze.make_maze(540, 80, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)

    maze.make_maze(840, 80, width=80, height=12, cellwidth=100, cellheight=75, wallthickness=20)
    
    
#    framework.grabbables.append((brick.Balloon(radius=15, num_pts=6, x=300, y=500)))
#    framework.grabbables[0].shape.layers = 0b1000
#    framework.grabbables[0].shape.group = 2

#    framework.primitives.append(framework.grabbables[0])
#    framework.space.add(framework.grabbables[0].body)
#    framework.space.add(framework.grabbables[0].shape)

#    framework.grabbables.append((brick.Balloon(radius=15, num_pts=10, x=115, y=525)))
#    framework.grabbables[1].shape.layers = 0b1000
#    framework.grabbables[1].shape.group = 2

#    framework.primitives.append(framework.grabbables[1])
#    framework.space.add(framework.grabbables[1].body)
#    framework.space.add(framework.grabbables[1].shape)

    candies = []
    for i in range(100):
        candies.append(sprite.Basic_Sprite("images/candy.png",500,300,width=10,height=8,mass=.1))
    for candy in candies:
        framework.space.add(candy.shape)
        framework.space.add(candy.body)
        candy.add(framework.characters)
    framework.grabbables.extend(candies)

    barrel = sprite.Basic_Sprite("images/barrel.png",430,0,width=15,height=33,mass=10,jumpable=1,offset=(0,-1))
    framework.space.add(barrel.shape)
    framework.space.add(barrel.body)
    barrel.add(framework.characters)

    global airship1
    airship1 = airship.Airship()
    

    pygame.mixer.music.load("I-Want-Candy.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
