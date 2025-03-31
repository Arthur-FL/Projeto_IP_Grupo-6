import pygame
from pygame.math import Vector2

class defense(pygame.sprite.Sprite):

        def __init__(self, game, pos):

                self.game = game
                self.groups = self.game.all_sprites_group, self.game.defense_group
                pygame.sprite.Sprite.__init__(self, self.groups)


                self.image = pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (50,50))
                self.pos = Vector2(pos)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
                self.pos[1] += 25

                #atributos diferentes nas torres
                self.fire_rate = 10
                self.dano = 15
                self.range = 165
                #
                
                
                self.cooldown = 100

        def update(self):
                
                self.cooldown -= self.fire_rate 
                if self.cooldown <= 0:
                        for enemy in self.game.enemy_group:
                        
                                vector = enemy.pos - self.pos
                                dist = vector.length()

                                if dist <= self.range:
                                        enemy.vida -= self.dano
                                        self.cooldown = 100
                                        break


class def_type1(defense):
        def __init__(self, game, pos):
                super().__init__(game, pos)
                
                
                self.fire_rate = 10
                self.dano = 15
                self.range = 165

class def_type2(defense):
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.fire_rate = 10
                self.dano = 15
                self.range = 220

class def_type3(defense):
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.fire_rate = 10
                self.dano = 15
                self.range = 100

                




              