import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, img):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.speed = 1.5
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self): # Método que executa o movimento do inimigo
        self.move()

    def move(self): # Método que define o movimento do inimigo
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos