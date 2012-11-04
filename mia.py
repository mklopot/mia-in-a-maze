import pygame
import pymunk
import glob

class Mia(pygame.sprite.Sprite):

    def __init__(self, image="images/mia/mia-front-0.png", x=100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load(image)
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.body = pymunk.Body(10,pymunk.inf)
        self.body.position = x,y
        self.shape = pymunk.Poly.create_box(self.body, (17,30))
        self.shape.elasticity = 0
        self.shape.friction = .6
        self.body.velocity_limit = 300
        self.shape.collision_type = 2
        
        self.can_jump = True
        
        
        self.imagelist_left = map(pygame.image.load, sorted(glob.glob('images/mia/mia-left-*.png')))
        self.imagelist_right = map(pygame.image.load, sorted(glob.glob('images/mia/mia-right-*.png')))
        self.left_counter = 0
        self.right_counter = 0
        
        self.animation_counter_max = 6
        self.animation_counter = self.animation_counter_max
     
        
    def update(self):
        self.rect.center = self.body.position
        
        self.animation_counter -= 1
        if self.animation_counter == 0:
            self.animation_counter = self.animation_counter_max
            if abs(self.body.velocity.x) < .1:
                self.image = self.image_default
            elif self.body.velocity.x > 0:
                self.animate_right()
            else:
                self.animate_left()
        
        
    def moveleft(self):
        self.body.apply_impulse((-200,0))
    
    def moveright(self):
        self.body.apply_impulse((200,0))
                
    def jump(self):
        self.body.apply_impulse((0,-500))
        
    def movedown(self):
        self.image = self.image_default

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
