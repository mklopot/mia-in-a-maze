import pygame
import pymunk
import glob

class Mia(pygame.sprite.Sprite):

    def __init__(self, image="images/mia/mia-front-0.png", x=100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.imagelist_left = map(pygame.image.load, sorted(glob.glob('images/mia/mia-left-*.png')))
        
        self.imagelist_right = map(pygame.image.load, sorted(glob.glob('images/mia/mia-right-*.png')))
        self.left_counter = 0
        self.right_counter = 0
        
        self.animation_counter_max = 6
        self.animation_counter = self.animation_counter_max
     
        
    def moveleft(self):
        self.rect.left -=1
        self.animation_counter -=1
        if self.animation_counter == 0:
            self.animation_counter = self.animation_counter_max
            self.animate_left()
    
    def moveright(self):
        self.rect.left +=1
        self.animation_counter -=1
        if self.animation_counter == 0:
            self.animation_counter = self.animation_counter_max
            self.animate_right()
                
    def jump(self):
        pass
        
    def movedown(self):
        pass

    def animate_left(self):
        self.image = self.imagelist_left[self.left_counter]
        self.left_counter += 1
        if self.left_counter > (len(self.imagelist_left) - 1):
            self.left_counter = 0
        
    def animate_right(self):
        self.image = self.imagelist_right[self.right_counter]
        self.right_counter += 1
        if self.right_counter > (len(self.imagelist_right) - 1):
            self.right_counter = 0
