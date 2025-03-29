
import pygame
from pygame.math import Vector2
import random
from coin import *


class Enemy(pygame.sprite.Sprite):
    
    
    def __init__(self, waypoints):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 1.5
        self.image = pygame.image.load('Assets/enemy1.webp').convert_alpha()
        self.dano = 1
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.final = False
        self.morto = False
        

    def update(self): # Método que executa o movimento do inimigo
        if not self.morto:
            self.move()
        else:
            self.drop()

    def move(self): # Método que define o movimento do inimigo
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        dist = self.movement.length()
       
        # passa para o proximo waypoint quando o inimigo ficar proximo do waypoint atual
        if dist <= self.speed:
            if self.target_waypoint < len(self.waypoints) - 1:
                self.target_waypoint += 1
                
                #
                self.morto = True
            #se acabou todos os waypoints n faz nada
            else:
                self.final = True

        self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos
    
    def drop(self):
        
        drop = coin(self.pos)
        return drop


class enem_type1(Enemy):
    
    def __init__(self, waypoints):
        super().__init__(waypoints)
        
        self.speed = 5
        self.health = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo1.png').convert_alpha()

  
class enem_type2(Enemy):
    def __init__(self, waypoints):
        super().__init__(waypoints)
        
        self.speed = 10
        self.health = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo2.png').convert_alpha()


class enem_type3(Enemy):
    def __init__(self, waypoints):
        super().__init__(waypoints)
        
        self.speed = 15
        self.health = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo3.png').convert_alpha()
  