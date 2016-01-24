#!/usr/bin/python

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import math

import framework
import keyinput
#import level1 

currentlevel = __import__("level1")

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+600)



def init():
    framework.init()
    currentlevel.level()   

def main():
    levelsize = currentlevel.level_size()
    while True:
        metainput = keyinput.getinput(currentlevel.player)
        if metainput == 0:
            currentlevel.player = currentlevel.playable[0]
        if metainput == 1:
            currentlevel.player = currentlevel.playable[1]
        
        scroll_x, scroll_y = 0, 0
        if currentlevel.player.rect.center[0] < framework.scrolling_margin:
            scroll_x = -(framework.scrolling_margin - currentlevel.player.rect.center[0]) * .1      
            framework.scrolling.x += scroll_x      
        if currentlevel.player.rect.center[1] < framework.scrolling_margin:
            scroll_y = -(framework.scrolling_margin - currentlevel.player.rect.center[1]) * .1      
            framework.scrolling.y += scroll_y      
        if currentlevel.player.rect.center[0] > framework.viewport_width - framework.scrolling_margin:
            scroll_x = (currentlevel.player.rect.center[0] - framework.viewport_width + framework.scrolling_margin ) * .1
            framework.scrolling.x += scroll_x 
        if currentlevel.player.rect.center[1] > framework.viewport_height - framework.scrolling_margin:
            scroll_y = (currentlevel.player.rect.center[1] - framework.viewport_height + framework.scrolling_margin) * .1
            framework.scrolling.y += scroll_y      


        #framework.screen.fill(THECOLORS["lightblue"])
        colormod = 165- int(abs((currentlevel.player.body.position.y - 700) / 40)) % 165
        #framework.screen.fill(pygame.Color(115,165,250))
        framework.screen.fill(pygame.Color(115,colormod,250))

        ## Wrap Around
        max_x, max_y = levelsize
        for character in framework.characters:
            if character.body.position.x > max_x:
                character.body.position.x -= max_x
                if character is currentlevel.player:
                    framework.scrolling.x -= max_x
                    if character.vehicle:
                        character.vehicle.body.position.x -= max_x
                        character.vehicle.balloon.body.position.x -= max_x
            if character.body.position.x < 0:
                character.body.position.x += max_x
                if character is currentlevel.player:
                    framework.scrolling.x += max_x
                    if character.vehicle:
                        character.vehicle.body.position.x += max_x
                        character.vehicle.balloon.body.position.x += max_x
            character.body.position.y = character.body.position.y % max_y

        for primitive in framework.primitives:
            primitive.body.position.x = primitive.body.position.x % max_x
            primitive.body.position.y = primitive.body.position.y % max_y


        framework.characters.update()
        
        framework.screen.blit(framework.static_surface,(-int(framework.scrolling[0]),-int(framework.scrolling[1])))
        framework.screen.blit(framework.static_surface,(-int(framework.scrolling[0] - levelsize[0]),-int(framework.scrolling[1])))
        framework.screen.blit(framework.static_surface,(-int(framework.scrolling[0] + levelsize[0]),-int(framework.scrolling[1])))

        for primitive in framework.primitives:
            primitive.update()
            
        framework.characters.draw(framework.screen)
       
        framework.clock.tick(70) 
        framework.space.step(1/70.0)
        if framework.debug:
            framework.screen.blit(framework.font.render("fps: " + str(framework.clock.get_fps()), 1, THECOLORS["green"]), (0,0))
            framework.screen.blit(framework.font.render("shapes: " + str(len(framework.space.shapes)), 1, THECOLORS["green"]), (0,20))
            if currentlevel.airship1:
                framework.screen.blit(framework.font.render("buoyancy: " + str((currentlevel.airship1.balloon.buoyancy[1])), 1, THECOLORS["green"]), (0,40))

        pygame.display.flip()

if __name__ == '__main__':
    init()
    sys.exit(main())
    pygame.quit()
