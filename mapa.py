import pygame


class map:
    def __init__(self):
        self.waypoints = [(0,360), (175, 360), (175, 160), (390, 160), (390, 440), (680, 440), (680, 300), (1121, 300)]
        self.imagem = pygame.image.load('Assets/pathtd.png').convert_alpha()