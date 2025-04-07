import pygame
import random
from collide_detector import *
class coin(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.dropped_items_group
        pygame.sprite.Sprite.__init__(self, self.groups)


        self.pos = (pos[0] + random.randint(-40,40), pos[1] + random.randint(-40,40)) # randomiza a posição um pouco
        self.image = pygame.transform.scale(pygame.image.load('Assets/coin.png'), (50,50)) 
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):

        if player_collide(self, self.game.player):
            self.game.money += 1
            for group in self.groups:
                group.remove(self)
        
        pass

