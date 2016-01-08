import pygame
from pygame.locals import *


def getinput(actor):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked 'close'
            pygame.quit() 
        elif event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                actor.moveleft()
            elif event.key == K_RIGHT:
                actor.moveright()
            elif event.key == K_UP:
 	        actor.jump()
            elif event.key == K_DOWN:
                actor.movedown()
            elif event.key == K_g:
                actor.grab()
            elif event.key == K_d:
                actor.drop()
            elif event.key == K_c | KMOD_LCTRL:
                pygame.quit()
                
      


