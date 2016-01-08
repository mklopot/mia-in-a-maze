#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

#debug = False
debug = True

def init():
    global viewport_width
    viewport_width = 800
    global viewport_height
    viewport_height = 600

    pygame.mixer.init()
    pygame.init()
    global screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mia in a Maze")
    pygame.key.set_repeat(10)
    
    global clock
    clock = pygame.time.Clock()

    global font
    font = pygame.font.SysFont("Arial", 16)
    
    global space
    space = pymunk.Space()
    space.collision_bias = pow(1.0 - 0.1, 70.0)
    space.gravity = (0.0, 900.0)
    space.iterations = 5
    #space.idle_speed_threshold = 20
    space.collision_slop = .0001
    space.damping = .99

    global scrolling
    scrolling = pymunk.Vec2d(0,0)
    global scrolling_margin
    scrolling_margin = 200
    
    global characters
    characters = pygame.sprite.Group()

    global footcontact_handler
    def footcontact_handler(space,arbiter):
        arbiter.shapes[0].owner.footcontact = True
        return True
    space.add_collision_handler(2,1, post_solve=footcontact_handler)
    
    global primitives
    primitives = []
    
    global grabbables
    grabbables = []

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
