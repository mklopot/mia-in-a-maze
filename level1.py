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
    player = mia.Mia(x=330,y=100)
    framework.space.add(player.body)
    for shape in player.shapes:
        framework.space.add(shape)
    player.add(framework.characters)    

    player2 = cassie.Cassie(x=630,y=100)
    framework.space.add(player2.body)
    for shape in player2.shapes:
        framework.space.add(shape)
    player2.add(framework.characters)    
    
    global playable
    playable = [player, player2]

    npcs = [doomimp.DoomImp(x=230, y=350, target=player), doomimp.DoomImp(x=630, y=250, target=player), doomimp.DoomImp(x=580,y=660,target=player)]
#    npcs = []
    for npc in npcs:
        framework.space.add(npc.body)
        for shape in npc.shapes:
            framework.space.add(shape)
        npc.add(framework.characters)
            
    bricks = []
    for i in range(1,8):
        bricks.append(brick.Brick(size=40, x=300 + 125*i, y=6850))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=250, x=130+21*i))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=350, x=130+21*i))
    for i in range(1,20):
        bricks.append(brick.Brick(size=10, y=450, x=130+21*i))
    
    for brickinstance in bricks:    
        framework.primitives.append(brickinstance)
        framework.space.add(brickinstance.body)
        framework.space.add(brickinstance.shape)    
    
    staticbricks = []
    staticbricks.append(brick.StaticBrick(x=455, y=150, width=50, height=10))
    staticbricks.append(brick.StaticBrick(x=380, y=370, width=10, height=420))
    staticbricks.append(brick.StaticBrick(x=400, y=1040, width=800, height=10))

    for staticbrick in staticbricks:
        framework.space.add(staticbrick.shape)

    boundary = []    
    boundary.append(brick.StaticBrick(x=1500, y=7000, width=3000, height=10))
    boundary.append(brick.StaticBrick(x=1500, y=10, width=3000, height=100,invisible=True))
    for bound in boundary:
        framework.space.add(bound.shape)

    maze.make_maze(130, 180, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)    

    maze.make_maze(570, 180, width=8, height=4, cellwidth=70, cellheight=65, wallthickness=10)

    maze.make_maze(870, 180, width=80, height=12, cellwidth=100, cellheight=75, wallthickness=20)
    
    
    framework.grabbables.append((brick.Balloon(radius=15, num_pts=6, x=330, y=600)))
    framework.grabbables[0].shape.layers = 0b1000
    framework.grabbables[0].shape.group = 2

    framework.primitives.append(framework.grabbables[0])
    framework.space.add(framework.grabbables[0].body)
    framework.space.add(framework.grabbables[0].shape)

    framework.grabbables.append((brick.Balloon(radius=15, num_pts=10, x=145, y=625)))
    framework.grabbables[1].shape.layers = 0b1000
    framework.grabbables[1].shape.group = 2

    framework.primitives.append(framework.grabbables[1])
    framework.space.add(framework.grabbables[1].body)
    framework.space.add(framework.grabbables[1].shape)

    candies = []
    for i in range(10):
        candies.append(sprite.Basic_Sprite("images/candy.png",530,400,width=10,height=8,mass=.1))
    for candy in candies:
        framework.space.add(candy.shape)
        framework.space.add(candy.body)
        candy.add(framework.characters)
    framework.grabbables.extend(candies)

    barrel = sprite.Basic_Sprite("images/barrel.png",460,100,width=15,height=33,mass=10,jumpable=1,elasticity=1,offset=(0,-1))
    framework.space.add(barrel.shape)
    framework.space.add(barrel.body)
    barrel.add(framework.characters)

    global airship1
    airship1 = airship.Airship(x=500,y=850)
    

    pygame.mixer.music.load("I-Want-Candy.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)

def level_size():
    return (3000,7300)

def respawn_point(character):
    return (50,50)
def respawn_velocity(character):
    return (0,0)
