import pygame
from game1 import *
import random
class Player:
    def __init__(self):
        self.xcord = 400
        self.ycord = 400
        self.image = pygame.image.load("assets/player2.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 3
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    
    def draw(self):
        window.blit(self.image,(self.xcord,self.ycord))
    def tick(self,keys):
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
        if keys[pygame.K_d]:
            if self.xcord + self.speed >= bwidth - self.width:
                pass
            else:
                self.xcord += self.speed

        if keys[pygame.K_a]: 
            if self.xcord - self.speed <= 0:
                pass
            else:
                self.xcord -= self.speed

        if keys[pygame.K_w]: 
            if self.ycord - self.speed <= 0:
                pass
            else:
                self.ycord -= self.speed

        if keys[pygame.K_s]:
            if self.ycord + self.speed >= bheight - self.height:
                pass
            else:
                self.ycord += self.speed
        
    

class Cash:
    def __init__(self):
        self.xcord = random.randint(0, 1280)
        self.ycord = random.randint(0, 720)
        self.image = pygame.image.load("assets/cash.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    def draw(self):
        window.blit(self.image, (self.xcord, self.ycord))

    def genCash(self):
        self.draw(random.randint(0,bwidth),random.randint(0,bheight))
    

class Farmland:
    def __init__(self):
        self.xcord = 200 
        self.ycord = 200
        self.image = pygame.image.load("assets/farmland.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    def draw(self):
        window.blit(self.image,(self.xcord,self.ycord))
    def tick(self):
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
class Sunflower:
    def __init__(self):
        self.xcord = 0
        self.ycord = 0
        self.image = pygame.image.load("assets/sunflower.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    def tick(self):
        self.hitbox = pygame.Rect(self.xcord,self.ycord,self.width,self.height)
    def draw(self):
        window.blit(self.image,(self.xcord,self.ycord))





