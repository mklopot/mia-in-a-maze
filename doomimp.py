import pygame
import pymunk
import glob

class DoomImp(pygame.sprite.Sprite):

    def __init__(self, target, image="images/imp/imp.png", x=100, y=100):
        pygame.sprite.Sprite.__init__(self)
        self.image_default = pygame.image.load(image)
        self.image = self.image_default
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.body = pymunk.Body(30,pymunk.inf)
        self.body.position = x,y
        self.body.velocity_limit = 300
        
        self.main_shape = pymunk.Circle(self.body, 17, offset=(0,-4))
        self.head_shape = pymunk.Circle(self.body, 6, offset=(0,-22)) 
        self.feet_shape = pymunk.Poly(self.body, [(4,5),(-4,5),(-4,21),(4,21)])
        
        self.shapes = [self.main_shape, self.feet_shape, self.head_shape]
              
        self.main_shape.elasticity = self.feet_shape.elasticity = 0.3
        self.feet_shape.friction = 1
        self.main_shape.friction = 0
        self.feet_shape.collision_type = 2
        self.head_shape.collision_type = 1
        self.feet_shape.owner = self
        
        self.footcontact = False
        
        self.imagelist_left = map(pygame.image.load, sorted(glob.glob('images/imp/imp-left-*.png')))
        self.imagelist_right = map(pygame.image.load, sorted(glob.glob('images/imp/imp-right-*.png')))
        self.left_counter = 0
        self.right_counter = 0
        
        self.animation_counter_max = 8
        self.animation_counter = self.animation_counter_max
     
        self.target = target
        
    def update(self):
        self.rect.center = self.body.position
        
        self.animation_counter -= 1
        if self.animation_counter == 0:
            self.animation_counter = self.animation_counter_max
            if abs(self.body.velocity.x) < 18:
                self.image = self.image_default
            elif self.body.velocity.x > 0:
                self.animate_right()
            else:
                self.animate_left()
        
        self.attack(self.target)
        
    def moveleft(self):
        self.body.apply_impulse((-540,0))
    
    def moveright(self):
        self.body.apply_impulse((540,0))
                
    def jump(self):
        if self.footcontact:
            self.body.apply_impulse((0,-30000))
            self.footcontact = False
            
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
    
    def attack(self, target):
        if (abs(target.body.position.x - self.body.position.x) < 100) and ((self.body.position.y - target.body.position.y) > 60):
            self.jump()
        if target.body.position.x > self.body.position.x:
            self.moveright()
        else:
            self.moveleft()
