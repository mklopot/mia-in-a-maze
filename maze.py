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
    space.gravity = (0.0, -900.0)
    
    global player
    player=mia.Mia()
    
    global players
    players = pygame.sprite.Group()
    player.add(players)

def main():
    while True:
        keyinput.getinput(player)

        screen.fill(THECOLORS["lightblue"])
        players.draw(screen)

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
