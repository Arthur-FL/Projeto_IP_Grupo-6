import pygame
import random


class health_drop(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/heart.png').convert_alpha()
        self.pos = (9999,9999)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.timer = random.randint(60,360)
        # if passou o mouse por cima:
        #   coletar
        #   e aumenta a vida
        
    def update(self):
        self.timer -=1
        if self.timer == 0:
            self.image = pygame.image.load('Assets/heart.png').convert_alpha()
            self.pos = (random.randint(100,900),random.randint(100,600))
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

        pass