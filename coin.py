import pygame
import random
class coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.pos = (pos[0] + random.randint(0,20), pos[1] + random.randint(0,20))
        self.image = pygame.transform.scale(pygame.image.load('Assets/coin.png'), (50,50)) 
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pass

