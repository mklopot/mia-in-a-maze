import pygame
import pymunk
import glob
import math

import framework

class AirshipGondola(pygame.sprite.Sprite):
    def __init__(self,x=600,y=5,angle=0,angular_velocity=0):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load("images/airship-gondola.png").convert_alpha()
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        offset = (0,0) # center of gravity
        points_bow = [(-156, -33), (-99, 14), (-82, -2)]
        #points_midship = [(57,47),(74,32),(142,65),(216,65),(251,62),(261,53),(227,32)]        
        #points_midship = [(-99, 14), (-82, -1), (-14, 32), (60, 32), (95, 29), (105, 20), (71, -1)]
        points_midship = [(-82, -1), (-99, 14), (-14, 32), (60, 32), (95, 29), (105, 20),(71,-1)]
        points_stern = [(105, 20), (145, 13), (156, -21), (95, -17), (71, -1)]
        mass_bow = 10
        mass_midship = 10
        mass_stern = 10
        mass = mass_bow + mass_midship + mass_stern
        moment = pymunk.moment_for_poly(mass_bow,points_bow,offset) + pymunk.moment_for_poly(mass_stern,points_stern,offset)
        #moment = pymunk.moment_for_poly(mass_bow,points_bow,offset) + pymunk.moment_for_poly(mass_midship,points_midship,offset) + pymunk.moment_for_poly(mass_stern,points_stern,offset)
        self.body = pymunk.Body(mass,moment)
        self.body.position = x,y
        self.body.angular_velocity = angular_velocity
        self.body.velocity_limit = 300
        

        self.bow = pymunk.Poly(self.body, points_bow, offset)
        self.midship = pymunk.Poly(self.body, points_midship, offset)
        self.stern = pymunk.Poly(self.body, points_stern, offset)

       # self.shape.layers = self.shape.layers ^ 0b1000
        
        #self.shapes = [self.bow, self.stern]
        self.shapes = [self.bow, self.midship, self.stern]
        
        for shape in self.shapes:      
            shape.elasticity = 0
            shape.friction = 1
            shape.collision_type = 1    # 0 - can't jump off of it; 1 - can jump when standing on it
        

    def update(self):
        self.rect.center = self.body.position - framework.scrolling
        self.image = framework.rot_center(self.image_default, math.degrees(-self.body.angle))
        if framework.debug:
            for shape in self.shapes:
                scrolled_points = [point - framework.scrolling for point in shape.get_vertices()]
                pygame.draw.polygon(framework.screen, pygame.color.THECOLORS["green"], scrolled_points, True)
