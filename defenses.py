import pygame
from pygame.math import Vector2

class defense(pygame.sprite.Sprite):

        def __init__(self, game, pos):

                self.game = game
                self.groups = self.game.all_sprites_group, self.game.defense_group
                pygame.sprite.Sprite.__init__(self, self.groups)


                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))
                self.pos = Vector2(pos)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
                self.pos[1] += 25

                #atributos diferentes nas torres
                self.fire_rate = 1
                self.dano = 1 # dano ou tipo de projetil
                self.range = 1
                self.cost = 0
                #
                
                
                self.cooldown = 1000

        def update(self):
                
                
                if self.cooldown <= 0:
                        for enemy in self.game.enemy_group:
                        
                                vector = enemy.pos - self.pos
                                dist = vector.length()

                                if dist <= self.range:
                                        
                                        self.shoot(enemy)
                                        self.cooldown = 1000
                                        break
                
                else:
                        self.cooldown -= self.fire_rate 

        def shoot(self, enemy):
                enemy.hp -= self.dano


class def_type1(defense): # basico
        def __init__(self, game, pos):
                super().__init__(game, pos)
                
                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))
                
                self.fire_rate = 18
                self.dano = 30
                self.range = 175
                self.cost = 0

class def_type2(defense): # range alto, firerate baixo
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))

                self.fire_rate =  12
                self.dano = 75
                self.range = 250
                self.cost = 0

class def_type3(defense): # range baixo, dps alto 
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))

                self.fire_rate = 100
                self.dano = 25
                self.range = 125
                self.cost = 0


class def_type4(defense): # empurra os inimigos :O
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))

                self.fire_rate = 3
                self.dano = 10
                self.range = 160
                self.cost = 0

        def shoot(self,enemy):
                enemy.target_waypoint = max(0, enemy.target_waypoint - 2)
                enemy.hp -= self.dano


   

 
class def_type5(defense): # taca fogo nos inimigos sla
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (60,60))

                self.fire_rate = 10
                self.dano = 0
                self.range = 150
                self.cost = 0

        def shoot(self,enemy):
                enemy.on_fire = True

                




              