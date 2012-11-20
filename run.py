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
import level1


def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)



def init():
    framework.init()
    level1.level()   

def main():
    while True:
        keyinput.getinput(level1.player)

        framework.screen.fill(THECOLORS["lightblue"])
        framework.characters.update()
        
        for primitive in framework.primitives:
            primitive.update()
            
        framework.characters.draw(framework.screen)
        #print level1.player.feet_shape.get_points()
        
        #draw_space(screen, space)
        
        framework.space.step(1/50.0)

        pygame.display.flip()
        framework.clock.tick(50)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
