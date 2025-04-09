import pygame
import random
from collide_detector import *

class drop_generator:

    def __init__(self, game):
        self.game = game
        self.timer = random.randint(300, 600)


    def update(self):
        self.timer -=1
        if self.timer == 0:
            pos = (random.randint(100,900),random.randint(100,600))
            tipo_item = random.randint(0,2)
            
            if tipo_item == 0:
                health_drop(self.game, pos)
            if tipo_item == 1:
                # gera um power-up(?)
                shield_Drop(self.game, pos)
            if tipo_item == 2:
                # gera outro tipo de item(?)
                health_drop(self.game, pos)

            # reseta o timer
            self.timer = random.randint(300, 600)

        

class health_drop(pygame.sprite.Sprite):

    def __init__(self, game, pos):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.dropped_items_group
        
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.pos = pos
        self.image = pygame.image.load('Assets/heart.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def update(self):

        
        #checa se o mouse passou por cima e coleta automaticamente.
        if player_collide(self, self.game.player):
            self.game.hp += 1
            self.kill()

class shield_Drop(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.dropped_items_group
        
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.pos = pos
        self.image =  pygame.transform.scale(pygame.image.load('Assets/shield.png'), (80,80))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def update(self):
        if player_collide(self, self.game.player):
            self.game.shield = True
            self.kill()
        
        
