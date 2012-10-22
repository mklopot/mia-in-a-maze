import pygame
import pymunk

class Mia(pygame.sprite.Sprite):

    def __init__(self, image="images/mia/mia-front-0.png", x=100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
     
        
    def moveleft(self):
        self.rect.left -=1
    
    def moveright(self):
        self.rect.left +=1
        
    def jump(self):
        pass
        
    def movedown(self):
        pass

