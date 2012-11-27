#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

def init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("MIa in a Maze")
    pygame.key.set_repeat(10)
    
    global clock
    clock = pygame.time.Clock()

    global space
    
    global footcontact_handler
    def footcontact_handler(space,arbiter):
        arbiter.shapes[0].owner.footcontact = True
        #print "footcontact set to True"    
        return True 
    
    space = pymunk.Space()
    space.gravity = (0.0, 900.0)
    space.iterations = 5
    #space.idle_speed_threshold = 20
    space.collision_slop = .001
    space.add_collision_handler(2,1, post_solve=footcontact_handler)
    
    global characters
    characters = pygame.sprite.Group()
    
    global primitives
    primitives = []
    
    global prize
