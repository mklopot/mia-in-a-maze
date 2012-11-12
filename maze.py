#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

from pymunk.pygame_util import draw_space

import framework
import keyinput
import mia
import doomimp

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)



def init():
    framework.init()
       
    global characters
    characters = pygame.sprite.Group()
    
    global player
    player = mia.Mia(x=300,y=450)
    framework.space.add(player.body)
    for shape in player.shapes:
        framework.space.add(shape)
    player.add(characters)    

    global npcs
    npcs = [doomimp.DoomImp(x=200, y=250, target=player), doomimp.DoomImp(x=700, y=150, target=player), doomimp.DoomImp(x=700,y=560,target=player)]
    for npc in npcs:
        framework.space.add(npc.body)
        for shape in npc.shapes:
            framework.space.add(shape)
        npc.add(characters)
            
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

def main():
    while True:
        keyinput.getinput(player)

        framework.screen.fill(THECOLORS["lightblue"])
        characters.update()
        
        pygame.draw.line(framework.screen, 0, (50,500), (500, 500), 5)
        pygame.draw.line(framework.screen, 0, (500,540), (550, 540), 5)
        pygame.draw.line(framework.screen, 0, (100,450), (450, 140), 5)
        
        characters.draw(framework.screen)
        print player.feet_shape.get_points()
        
        #draw_space(screen, space)
        
        framework.space.step(1/50.0)

        pygame.display.flip()
        framework.clock.tick(50)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
