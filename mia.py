import pygame
import pymunk
import glob
import math

import framework

class Mia(pygame.sprite.Sprite):

    def __init__(self, image="images/mia/mia-front-0.png", x=100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load(image)
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.body = pymunk.Body(10,pymunk.inf)
        self.body.position = x,y
        self.body.velocity_limit = 300
        
        self.main_shape = pymunk.Circle(self.body, 11, offset=(0,-5))
        self.main_shape.layers = self.main_shape.layers ^ 0b1000
        self.feet_shape = pymunk.Poly(self.body, [(3,5),(-3,5),(-3,15),(3,15)])
        
        self.shapes = [self.main_shape, self.feet_shape]
              
        self.main_shape.elasticity = self.feet_shape.elasticity = 0.3
        self.feet_shape.friction = .9
        self.main_shape.friction = .3
        self.feet_shape.collision_type = 2
        self.feet_shape.owner = self
        
        self.footcontact = False
        
        self.imagelist_left = map(pygame.image.load, sorted(glob.glob('images/mia/mia-left-*.png')))
        self.imagelist_right = map(pygame.image.load, sorted(glob.glob('images/mia/mia-right-*.png')))
        self.left_counter = 0
        self.right_counter = 0
        
        self.animation_counter_max = 8
        self.animation_counter = self.animation_counter_max

        self.grab_joint = None   
        
    def update(self):
        self.rect.center = self.body.position
        
        self.animation_counter -= 1
        if self.animation_counter == 0:
            self.animation_counter = self.animation_counter_max
            if abs(self.body.velocity.x) < .001:
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
        if self.footcontact:
            self.body.apply_impulse((0,-10000))
            #self.body.apply_impulse((0,-1000))
            self.footcontact = False
            
    def movedown(self):
        self.image = self.image_default

    def grab(self):
        if framework.prize and not self.grab_joint:
            if math.sqrt((self.body.position.x - framework.prize.body.position.x) ** 2 + (self.body.position.y - framework.prize.body.position.y) ** 2) < 50:
                 self.grab_joint = pymunk.SlideJoint(self.body, framework.prize.body, (0,0), (0,0), min=5, max=16)
                 framework.space.add(self.grab_joint)
        else:
            framework.space.remove(self.grab_joint)
            self.grab_joint = None

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
