#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

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
        
        if level1.player.rect.center[0] < framework.scrolling_margin:
            framework.scrolling.x -= framework.scrolling_margin - level1.player.rect.center[0]      
        if level1.player.rect.center[1] < framework.scrolling_margin:
            framework.scrolling.y -= framework.scrolling_margin - level1.player.rect.center[1]      
        if level1.player.rect.center[0] > framework.viewport_width - framework.scrolling_margin:
            framework.scrolling.x += level1.player.rect.center[0] - framework.viewport_width + framework.scrolling_margin 
        if level1.player.rect.center[1] > framework.viewport_height - framework.scrolling_margin:
            framework.scrolling.y += level1.player.rect.center[1] - framework.viewport_height + framework.scrolling_margin


        #framework.screen.fill(THECOLORS["lightblue"])
        framework.screen.fill(pygame.Color(115,165,250))
        framework.characters.update()
        
        for primitive in framework.primitives:
            primitive.update()
            
        framework.characters.draw(framework.screen)
        
        framework.space.step(1/50.0)
        framework.screen.blit(framework.font.render("fps: " + str(framework.clock.get_fps()), 1, THECOLORS["magenta"]), (0,0))
        framework.screen.blit(framework.font.render("shapes: " + str(len(framework.space.shapes)), 1, THECOLORS["magenta"]), (0,20))

        pygame.display.flip()
        framework.clock.tick(70)

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
