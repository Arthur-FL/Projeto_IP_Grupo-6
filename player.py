import pygame
from pygame.math import Vector2

class player(pygame.sprite.Sprite):

    def __init__(self, game):

        self.game = game
        self.groups = self.game.all_sprites_group, self.game.player_group
        pygame.sprite.Sprite.__init__(self, self.groups)


        self.image = pygame.transform.scale(pygame.image.load('Assets/player.png'), (80,80))
        self.pos = Vector2(500,500)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 8

    

    def update(self):
        


            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and self.pos[1]> 0:
                self.pos[1] -= self.speed
            if keys[pygame.K_a] and self.pos[0]> 0:
                    self.pos[0] -= self.speed
            if keys[pygame.K_s] and self.pos[1]< 720:
                    self.pos[1] += self.speed
            if keys[pygame.K_d] and self.pos[0]< 1080 :
                    self.pos[0] += self.speed

            self.rect.center = self.pos

