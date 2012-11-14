import pygame
import pymunk

import framework

class Brick():

    def __init__(self, size, x=400, y=400):
           
        self.body = pymunk.Body(20,20)
        self.body.position = x,y
                
         
        self.shape = pymunk.Poly.create_box(self.body, (size,size))
        
        self.shapes = [self.shape]
              
        self.shape.elasticity = 0
        self.shape.friction = .6
        self.shape.owner = self
        
    def update(self):
        pygame.draw.lines(framework.screen, 1, True, self.shape.get_points())       

        
