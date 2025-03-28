import pygame
import random


class health_drop(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/heart.png').convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # if passou o mouse por cima:
        #   coletar
        #   e aumenta a vida

        pass