import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 1.5
        self.image = pygame.image.load('Assets/inimigo1.png.webp').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self): # Método que executa o movimento do inimigo
        self.move()

    def move(self): # Método que define o movimento do inimigo
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        dist = self.movement.length()
       
        # passa para o proximo waypoint quando o inimigo ficar proximo do waypoint atual
        if dist <= self.speed:
            if self.target_waypoint != len(self.waypoints) - 1:
                self.target_waypoint += 1
           
            #se acabou todos os waypoints n faz nada
            # quando chega aqui é pra deletar o inimigo e fazer o player perder vida #provavelmente
            else:
                pass

        self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos
