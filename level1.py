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

def level():
    global player
    player = mia.Mia(x=300,y=450)
    framework.space.add(player.body)
    for shape in player.shapes:
        framework.space.add(shape)
    player.add(framework.characters)    

    npcs = [doomimp.DoomImp(x=200, y=250, target=player), doomimp.DoomImp(x=700, y=150, target=player), doomimp.DoomImp(x=700,y=560,target=player)]
    for npc in npcs:
        framework.space.add(npc.body)
        for shape in npc.shapes:
            framework.space.add(shape)
        npc.add(framework.characters)
            
    left_border = pymunk.Segment(pymunk.Body(), (0,0), (0, 600), 5)
    right_border = pymunk.Segment(pymunk.Body(), (800,0), (800, 600), 5)
    top_border = pymunk.Segment(pymunk.Body(), (0,0), (800, 0), 5)
    bottom_border = pymunk.Segment(pymunk.Body(), (0,600), (800, 600), 5)
    line = pymunk.Segment(pymunk.Body(), (50.0,500.0), (500.0, 500.0), 5)
    line1 = pymunk.Segment(pymunk.Body(), (500.0,540.0), (550.0, 540.0), 5)
    diag = pymunk.Segment(pymunk.Body(), (100.0,450.0), (450.0, 140.0), 5)
    segments = [left_border, right_border, top_border, bottom_border, line, line1, diag]
    
    for segment in segments:
        segment.elasticity = 0
        segment.friction = .9
        segment.collision_type = 1
        framework.space.add(segment)

