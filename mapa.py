import pygame


class map:
    def __init__(self):
        self.waypoints = [(-300,360), (175, 360), (175, 160), (390, 160), (390, 440), (680, 440), (680, 300), (1131, 300)]
        self.imagem = pygame.image.load('Assets/pathtd.png').convert_alpha()
        self.waves = [[1],[1,1],[1,2], [1,2,2,2,1],[3,3,3,3,3,3,3]] 