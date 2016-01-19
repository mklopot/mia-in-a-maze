import pygame
from pygame.color import *
import pygame.gfxdraw
import pymunk
import math

import framework
import level1

global visibility
visibility = 850

class StaticBrick():

    def __init__(self, width, height, x=300, y=400):
           
        self.body = pymunk.Body(None,None)
        
        points = [(-width/2, -height/2), (-width/2, height/2), (width/2,height/2), (width/2, -height/2)]        

        self.width = width
        self.height = height
                
        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = pymunk.Vec2d(x,y)
        
        self.shapes = [self.shape]
              
        self.shape.friction = 0.5
        self.shape.collision_type = 1
        self.shape.owner = self
        
        topleft = self.body.position - framework.scrolling - pymunk.Vec2d(self.width/2,self.height/2)
        rect = pygame.Rect(topleft[0],topleft[1],self.width,self.height)
        framework.static_surface.fill(THECOLORS["darkgrey"],rect)
        pygame.gfxdraw.rectangle(framework.static_surface, rect, THECOLORS["orange"])

    def update(self):
#        global visibility
#        if self.body.position.get_distance(level1.player.body.position) < visibility:
#            scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
        pass



class Brick():

    def __init__(self, size, x=400, y=400):
        points = [(-size, -size), (-size, size), (size,size), (size, -size)]
        mass = 1.0
        moment = pymunk.moment_for_poly(mass, points, (0,0))        
        
        self.body = pymunk.Body(mass, moment)
                
        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = x,y
        
        self.shapes = [self.shape]
              
        self.shape.elasticity = 1.5
        self.shape.friction = 1.0
        self.shape.collision_type = 1
        self.shape.owner = self
        
    def update(self):
        global visibility
        if self.body.position.get_distance(level1.player.body.position) < visibility:
          scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
          pygame.draw.polygon(framework.screen, THECOLORS["brown"], scrolled_points)
          pygame.draw.polygon(framework.screen, THECOLORS["black"], scrolled_points, True)


        

class Polygon():
    
    def __init__(self, radius, num_pts, x=300, y=400):
        points=[]
        for i in range(0, num_pts):
            angle = (i * 2 * math.pi / num_pts)
            ptx = radius * math.cos(angle)
            pty = radius * math.sin(angle)
            points.append((ptx, pty))

        
        mass = 1.7
        moment = pymunk.moment_for_poly(mass, points, (0,0))

        self.body = pymunk.Body(mass, moment)

        self.shape = pymunk.Poly(self.body, points, (0,0))

        self.body.position = x,y

        self.shapes = [self.shape]

        self.shape.friction = 0.2
        self.shape.collision_type = 0
        self.shape.owner = self

    def update(self):
        global visibility
        if self.body.position.get_distance(level1.player.body.position) < visibility:
            scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
            pygame.draw.polygon(framework.screen, THECOLORS["yellow"], scrolled_points)
            pygame.draw.polygon(framework.screen, THECOLORS["black"], scrolled_points, True)


class Balloon(Polygon):
    def update(self):
        global visibility
        if self.body.position.get_distance(level1.player.body.position) < visibility:
            scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
            pygame.draw.polygon(framework.screen, THECOLORS["red"], scrolled_points)
            pygame.draw.polygon(framework.screen, THECOLORS["black"], scrolled_points, True)

        self.body.apply_impulse((0,-110))

