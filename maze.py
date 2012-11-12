#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

from pymunk.pygame_util import draw_space

import keyinput
import mia
import doomimp

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)



def init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Awesome Maze")
    pygame.key.set_repeat(10)
    
    global clock
    clock = pygame.time.Clock()

    global space
    
    global footcontact_handler
    def footcontact_handler(space,arbiter):
        arbiter.shapes[0].owner.footcontact = True
        print "footcontact set to True"    
        return True 
    
    space = pymunk.Space()
    space.gravity = (0.0, 900.0)
    space.iterations = 3
    space.idle_speed_threshold = 20
    space.collision_slop = .001
    space.add_collision_handler(2,1, post_solve=footcontact_handler)
    

        
    global characters
    characters = pygame.sprite.Group()
    
    global player
    player = mia.Mia(x=300,y=450)
    space.add(player.body)
    for shape in player.shapes:
        space.add(shape)
    player.add(characters)    

    global npcs
    npcs = [doomimp.DoomImp(x=200, y=250, target=player), doomimp.DoomImp(x=700, y=150, target=player), doomimp.DoomImp(x=700,y=560,target=player)]
    for npc in npcs:
        space.add(npc.body)
        for shape in npc.shapes:
            space.add(shape)
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
        space.add(segment)

def main():
    while True:
        keyinput.getinput(player)

        screen.fill(THECOLORS["lightblue"])
        characters.update()
        
        pygame.draw.line(screen, 0, (50,500), (500, 500), 5)
        pygame.draw.line(screen, 0, (500,540), (550, 540), 5)
        pygame.draw.line(screen, 0, (100,450), (450, 140), 5)
        
        characters.draw(screen)
        print player.feet_shape.get_points()
        
        #draw_space(screen, space)
        
        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
