import pygame

def player_collide(sprite:pygame.sprite.Sprite, player = pygame.sprite.Sprite):
    
    #retorna True se o mouse estiver sobre o sprite
    return sprite.rect.colliderect(player)

