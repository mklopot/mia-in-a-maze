import pygame
import pymunk
import glob
import math

import framework

def myround(x, base=5):
    return int(base * round(float(x)/base))        

class Basic_Sprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y,angle=0,angular_velocity=0,width=10,height=10,mass=1,elasticity=0,friction=.8,offset=(0,0),jumpable=0):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load(image).convert_alpha()
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        points = [(-width, -height/2), (-width, height/2), (width,height/2), (width, -height/2)]        
        self.body = pymunk.Body(mass,pymunk.moment_for_poly(mass,points,offset))
        self.body.position = x,y
        self.body.angular_velocity = angular_velocity
        self.body.velocity_limit = 300
        

        self.shape = pymunk.Poly(self.body, points, offset)

       # self.shape.layers = self.shape.layers ^ 0b1000
        
        self.shapes = [self.shape]
              
        self.shape.elasticity = elasticity
        self.shape.friction = friction
        self.shape.collision_type = jumpable    # 0 - can't jump off of it; 1 - can jump when standing on it
 
        self.rotated_images = {}
        for i in range(0,360,5):
           self.rotated_images[i] = framework.rot_center(self.image_default, i) 


    def update(self):
        self.rect.center = self.body.position - framework.scrolling
        approx_angle = myround(math.degrees(-self.body.angle),5)
        self.image = self.rotated_images[approx_angle % 360] 
        if framework.debug:
            scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
            pygame.draw.polygon(framework.screen, pygame.color.THECOLORS["green"], scrolled_points, True)



        
        
    
                
            




