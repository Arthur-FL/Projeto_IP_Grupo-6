import pygame

def mouse_hover(sprite):
    #retorna True se o mouse estiver sobre o sprite
    return sprite.rect.collidepoint(pygame.mouse.get_pos())

