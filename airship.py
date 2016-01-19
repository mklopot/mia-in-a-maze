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
        points_midship = [(-82, -1), (-99, 14), (-14, 32), (60, 32), (95, 29), (105, 20),(71,-1)]
        points_stern = [(105, 20), (145, 13), (156, -21), (95, -17), (71, -1)]
        mass_bow = 10
        mass_midship = 10
        mass_stern = 10
        mass = mass_bow + mass_midship + mass_stern
        moment = pymunk.moment_for_poly(mass_bow,points_bow,offset) + pymunk.moment_for_poly(mass_stern,points_stern,offset)
        moment *= 3
        self.body = pymunk.Body(mass,moment)
        self.body.position = x,y
        self.body.angular_velocity = angular_velocity
        self.body.velocity_limit = 300
        

        self.bow = pymunk.Poly(self.body, points_bow, offset)
        self.midship = pymunk.Poly(self.body, points_midship, offset)
        self.stern = pymunk.Poly(self.body, points_stern, offset)

        
        self.shapes = [self.bow, self.midship, self.stern]
        self.balloon = None     
        for shape in self.shapes:      
            shape.owner = self
            shape.elasticity = .5
            shape.friction = pymunk.inf
            shape.collision_type = 3    # 0 - can't jump off of it; 1 - can jump when standing on it
        

    def update(self):
        self.rect.center = self.body.position - framework.scrolling
        self.image = framework.rot_center(self.image_default, math.degrees(-self.body.angle))

        self.body.angular_velocity = self.body.angular_velocity * .98
        self.body.angle *= .99

        if self.balloon:
            pygame.draw.aaline(framework.screen,pygame.color.THECOLORS["brown"],self.body.position - pymunk.Vec2d(105,0).rotated(self.body.angle) - framework.scrolling, self.balloon.body.position - pymunk.Vec2d(185,20).rotated(self.balloon.body.angle) - framework.scrolling)
            pygame.draw.line(framework.screen,pygame.color.THECOLORS["gray"],self.body.position - pymunk.Vec2d(102,0).rotated(self.body.angle) - framework.scrolling, self.balloon.body.position - pymunk.Vec2d(185,20).rotated(self.balloon.body.angle) - framework.scrolling)
            pygame.draw.line(framework.screen,pygame.color.THECOLORS["brown"],self.body.position + pymunk.Vec2d(115,0).rotated(self.body.angle) - framework.scrolling, self.balloon.body.position + pymunk.Vec2d(185,20).rotated(self.balloon.body.angle) - framework.scrolling)
            pygame.draw.line(framework.screen,pygame.color.THECOLORS["gray"],self.body.position + pymunk.Vec2d(112,0).rotated(self.body.angle) - framework.scrolling, self.balloon.body.position + pymunk.Vec2d(185,20).rotated(self.balloon.body.angle) - framework.scrolling)

        if framework.debug:
            for shape in self.shapes:
                scrolled_points = [point - framework.scrolling for point in shape.get_vertices()]
                pygame.draw.polygon(framework.screen, pygame.color.THECOLORS["green"], scrolled_points, True)
    
    def left(self):
        self.body.apply_impulse((-150,0),(0,20))
    def right(self):
        self.body.apply_impulse((150,0),(0,20))
    def down(self):
        if self.balloon:
            self.balloon.body.apply_impulse((0,500),(0,0))
    def up(self):
        if self.balloon:
            self.balloon.body.apply_impulse((0,-500),(0,0))

class AirshipBalloon(pygame.sprite.Sprite):
    def __init__(self,x=600,y=-20,angle=0,angular_velocity=0,buoyancy=pymunk.Vec2d(0,-8000)):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load("images/airship-balloon.png").convert_alpha()
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        offset = (0,0) # center of gravity
        points = [(-210, -7), (-196, -24), (-82, -56), (-26, -60), (27, -60), (83, -56), (197, -24), (212, -7), (212, 6), (197, 25), (83, 57), (27, 61), (-26, 61), (-82, 57), (-196, 25), (-210, 8)]
        mass = 10
        moment = pymunk.moment_for_poly(mass,points)
        self.body = pymunk.Body(mass,moment)
        self.body.position = x,y
        self.body.angular_velocity = angular_velocity
        self.body.velocity_limit = 300
        

        self.shape = pymunk.Poly(self.body, points)
        self.shapes = [self.shape]
        
        self.shape.elasticity = 1
        self.shape.friction = .5
        self.shape.collision_type = 1    # 0 - can't jump off of it; 1 - can jump when standing on it

        self.buoyancy = buoyancy
        self.body.apply_force(buoyancy)
        

    def update(self):
        self.rect.center = self.body.position - framework.scrolling
        self.image = framework.rot_center(self.image_default, math.degrees(-self.body.angle))
        if framework.debug:
            scrolled_points = [point - framework.scrolling for point in self.shape.get_vertices()]
            pygame.draw.polygon(framework.screen, pygame.color.THECOLORS["green"], scrolled_points, True)


class Airship():
    def __init__(self,x=600, y=-20, buoyancy = pymunk.Vec2d(0,-34000)):
        balloon = AirshipBalloon(x,y,buoyancy=buoyancy)
        gondola = AirshipGondola(x,y+80)
        self.balloon = gondola.balloon = balloon
        self.rope1 = pymunk.constraint.SlideJoint(balloon.body,gondola.body,(-185,0),(-105,0),0,240)
        self.rope2 = pymunk.constraint.SlideJoint(balloon.body,gondola.body,(185,0),(105,0),0,240)


        framework.space.add(balloon.body)
        framework.space.add(balloon.shape)
        balloon.add(framework.characters)
        framework.space.add(self.rope1)
        framework.space.add(self.rope2)

        framework.space.add(gondola.body)
        for shape in gondola.shapes:
            framework.space.add(shape)
        gondola.add(framework.characters)
