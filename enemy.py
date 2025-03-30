
import pygame
from pygame.math import Vector2
import random
from coin import *


class Enemy(pygame.sprite.Sprite):
    
    
    def __init__(self, game):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.enemy_group
        pygame.sprite.Sprite.__init__(self, self.groups)


        # waypoints de movimentação no mapa
        self.waypoints = game.mapa.waypoints
        self.target_waypoint = 1

        #atributos modificaveis entre tipos de inimigos
        self.speed = 1
        self.dano = 1
        self.vida = 1
   
        # atributos do sprite
        self.image = pygame.image.load('Assets/enemy1.webp').convert_alpha()
        self.pos = Vector2(self.waypoints[0])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        #
        
        self.final = False
        self.morto = False
        

    def update(self): # Método que executa o movimento do inimigo
        # inimigo esá vivo
        if not self.morto:
            self.move()
        # inimigo morreu
        else:
            self.drop()

        # inimigo chegou ao final do caminho
        if self.final:
            for group in self.groups:
                group.remove(self)
            self.game.hp -= self.dano


    def move(self): # Método que define o movimento do inimigo
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        dist = self.movement.length()
       
        # passa para o proximo waypoint quando o inimigo ficar proximo do waypoint atual
        if dist <= self.speed:
            if self.target_waypoint < len(self.waypoints) - 1:
                self.target_waypoint += 1
                
                #debug pra testar morte do inimigo -> mata o inimigo logo no primeiro checkpoint 
                self.morto = True
                # se acabou todos os waypoints, o monstro chegou no final
            else:
                self.final = True


        self.pos += self.movement.normalize() * self.speed
        self.rect.center = self.pos
    
    def drop(self):
        
        drop = coin(self.game, self.pos)
        self.game.all_sprites_group.add(drop)
        self.game.dropped_items_group.add(drop)

        for group in self.groups:
            group.remove(self)
        


class enem_type1(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 5
        self.vida = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo1.png').convert_alpha()

  
class enem_type2(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 10
        self.vida = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo2.png').convert_alpha()


class enem_type3(Enemy):
    def __init__(self, game):
        super().__init__(game)
        
        self.speed = 15
        self.vida = 100
        self.dano = 1
        self.image = pygame.image.load('Assets/inimigo3.png').convert_alpha()
  