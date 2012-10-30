#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

import keyinput
import mia

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
    space = pymunk.Space()
    space.gravity = (0.0, 900.0)
    
    global player
    player=mia.Mia(y=450)
    space.add(player.body, player.shape)
    
    global players
    players = pygame.sprite.Group()
    player.add(players)
    
    left_border = pymunk.Segment(pymunk.Body(), (0,0), (0, 600), 0.0)
    right_border = pymunk.Segment(pymunk.Body(), (800,0), (800, 600), 0.0)
    top_border = pymunk.Segment(pymunk.Body(), (0,0), (800, 0), 0.0)
    bottom_border = pymunk.Segment(pymunk.Body(), (0,600), (800, 600), 0.0)
    line = pymunk.Segment(pymunk.Body(), (50.0,500.0), (500.0, 500.0), 0.0)
    segments = [left_border, right_border, top_border, bottom_border, line]
    
    for segment in segments:
        segment.elasticity = 0
        segment.friction = .5
        space.add(segment)

def main():
    while True:
        keyinput.getinput(player)

        screen.fill(THECOLORS["lightblue"])
        players.update()
        
        pygame.draw.line(screen, 0, (50,500), (500, 500))
        
        players.draw(screen)
        print player.shape.get_points()

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
