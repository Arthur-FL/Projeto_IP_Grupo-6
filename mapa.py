import pygame


class map:
    def __init__(self):
        self.waypoints = [(-450,360), (-100,360), (175, 360), (175, 160), (390, 160), (390, 440), (680, 440), (680, 300), (1131, 300)]
        self.imagem = pygame.image.load('Assets/pathtd.png').convert_alpha()
        self.waves = [[1], # wave 1
                      [1,1], # wave 2
                      [1,2], # wave 3
                      [1,2,2,2,1], # wave 4
                      [3,3,3,3,3,3,3], # wave 5
                      [3,3,3,3,3,3,3,1,1,1,1,1,2], # wave 6
                      [3,3,2,2,2,2,2,2,2,2,2,2,2], # wave 7
                      [3,3,3,3,1,1,1,1,1,1,1,3,3], # wave 8
                      [1,2,2,2,2,2,2,1,1,1,1,1,1,1,3,3,3,3], # wave 9
                      [3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3], # wave 10
                      [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1], # wave 11
                      [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,2,2,2,2], # wave 12
                      [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,3,3,3,3,3,3,3,3], # wave 13
                      [1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,3,3,3,1,1,1,1,3,3,3,3], # wave 14
                      [1,2,2,2,2,2,2,2,3,3,3,3,3,3,1,1,1,1,1,3,3,3,3,3,3,3,3,2,1,4], # wave 15
                      ]