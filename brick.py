import pygame
from pygame.color import *
import pymunk
import math

import framework


class StaticBrick():

    def __init__(self, width, height, x=300, y=400):
           
        self.body = pymunk.Body(None,None)
        
        points = [(-width/2, -height/2), (-width/2, height/2), (width/2,height/2), (width/2, -height/2)]        
        
        #self.body = framework.space.static_body
                
        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = x,y
        #self.shape = pymunk.Poly.create_box(self.body, (size,size))
        
        self.shapes = [self.shape]
              
        #self.shape.elasticity = 0
        self.shape.friction = 1.0
        self.shape.collision_type = 1
        self.shape.owner = self
        
    def update(self):
        pygame.draw.polygon(framework.screen, THECOLORS["darkgrey"], self.shape.get_points())       
        pygame.draw.polygon(framework.screen, THECOLORS["black"], self.shape.get_points(), True)


class Brick():

    def __init__(self, size, x=400, y=400):
           
        #self.body = pymunk.Body(10,200)
        
        points = [(-size, -size), (-size, size), (size,size), (size, -size)]
        mass = 1.0
        moment = pymunk.moment_for_poly(mass, points, (0,0))        
        
        self.body = pymunk.Body(mass, moment)
                
        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = x,y
        #self.shape = pymunk.Poly.create_box(self.body, (size,size))
        
        self.shapes = [self.shape]
              
        self.shape.elasticity = 1.5
        self.shape.friction = 1.0
        self.shape.collision_type = 1
        self.shape.owner = self
        
    def update(self):
        pygame.draw.polygon(framework.screen, THECOLORS["brown"], self.shape.get_points())       
        pygame.draw.polygon(framework.screen, THECOLORS["black"], self.shape.get_points(), True)
        

class Star():
    
    def __init__(self, outer_radius, inner_radius, num_pts, x=300, y=400):
        points=[]
        for i in range(0, num_pts):
            angle = (i * 2 * math.pi / num_pts)
            ptx = outer_radius * math.cos(angle)
            pty = outer_radius * math.sin(angle)
            points.append((ptx, pty))

#            angle = (i * 2 * math.pi / num_pts) + math.pi / num_pts
#            ptx = inner_radius * math.cos(angle)
#            pty = inner_radius * math.sin(angle)
#            points.append((ptx, pty))
        
        mass = 0.5
        moment = pymunk.moment_for_poly(mass, points, (0,0))

        self.body = pymunk.Body(mass, moment)

        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = x,y

        self.shapes = [self.shape]

        self.shape.friction = 1.0
        self.shape.collision_type = 0
        self.shape.owner = self

    def update(self):
        pygame.draw.polygon(framework.screen, THECOLORS["yellow"], self.shape.get_points())
        pygame.draw.polygon(framework.screen, THECOLORS["black"], self.shape.get_points(), True)

