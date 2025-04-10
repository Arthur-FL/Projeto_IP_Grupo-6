import pygame
from pygame.math import Vector2



def player_collide(sprite:pygame.sprite.Sprite, player = pygame.sprite.Sprite):
    
    return sprite.rect.colliderect(player)

def point_near_path(point, path, threshold=50):  #threshold define a distancia minima permitida entre a defesa e o caminho dos inimigos

                        point = Vector2(point)
                        for i in range(len(path) - 1):
                            start = Vector2(path[i])
                            end = Vector2(path[i + 1])
                            closest = start + (end - start) * max(0, min(1, (point - start).dot(end - start) / (end - start).length_squared()))
                            if point.distance_to(closest) < threshold:
                                return True
                        return False

def mouse_hover(sprite):
    #retorna True se o mouse estiver sobre o sprite
    return sprite.rect.collidepoint(pygame.mouse.get_pos())