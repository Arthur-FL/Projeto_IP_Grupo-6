import pygame
from pygame.math import *
import math

class projectile(pygame.sprite.Sprite):
    def __init__(self, game, pos, target):
        self.game = game
        self.groups = self.game.all_sprites_group, self.game.projectile_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        # atributos do sprite
        self.image = pygame.image.load('Assets/enemy1.png').convert_alpha()
        self.pos = Vector2(pos)
        self.target = target
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.move_direction = self.target - self.pos
        self.pos += self.move_direction.normalize() * 40
    

        #atributos de projetil
        self.speed = 10
        self.pierce = 2
        self.dano = 25
        self.life_time = 99999


        #
        self.hit_list = []
        

    def move(self):
        
        self.pos += self.move_direction.normalize() * self.speed
        self.rect.center = self.pos

    def update(self):
        self.move()

        collisions = pygame.sprite.spritecollide(self,self.game.enemy_group, False)
        
        for enemy in collisions:
            if enemy not in self.hit_list:
                enemy.hp -= self.dano
                self.pierce -= 1
                self.hit_list.append(enemy)
            if self.pierce <= 0:
                self.kill()

        self.life_time -= 1
        if self.life_time <= 0:
            self.kill()

    def rotate(self):
        angle = math.degrees(math.atan2(-self.move_direction[1], self.move_direction[0] ))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


        
class arrow(projectile):
    def __init__(self, game, pos, target):
        super().__init__(game, pos, target)
        
        self.speed = 10
        self.pierce = 2
        self.dano = 25
        self.image = pygame.image.load('Assets/arrow.png').convert_alpha()
        self.rotate()

class snipe(projectile):
    def __init__(self, game, pos, target):
        super().__init__(game, pos, target)
        
        self.speed = 45
        self.pierce = 1
        self.dano = 125
        self.image = pygame.image.load('Assets/arrow.png').convert_alpha()
        self.rotate()

class slash(projectile):
    def __init__(self, game, pos, target):
        super().__init__(game, pos, target)
        
        self.speed = 0
        self.pierce = 5
        self.dano = 10
        self.image = pygame.image.load('Assets/slash.png').convert_alpha()
        self.rotate()

        self.life_time = 15

class push_shot(projectile):
    def __init__(self, game, pos, target):
        super().__init__(game, pos, target)
        
        self.speed = 0.25
        self.pierce = 10
        self.dano = 10
        self.image = pygame.image.load('Assets/slash.png').convert_alpha()
        self.rotate()

        self.life_time = 50
            
    def update(self):
        self.move()

        collisions = pygame.sprite.spritecollide(self,self.game.enemy_group, False)
        
        for enemy in collisions:
            if enemy not in self.hit_list:
                enemy.hp -= self.dano
                if type(enemy) != 'enem_type4':
                    enemy.target_waypoint = max(0, enemy.target_waypoint - 2)
                self.pierce -= 1
                self.hit_list.append(enemy)
            
            if self.pierce <= 0:
                self.kill()

        self.life_time -= 1
        if self.life_time <= 0:
            self.kill()


class fire_shot(projectile):
    def __init__(self, game, pos, target):
        super().__init__(game, pos, target)
        
        self.speed = 8
        self.pierce = 3
        self.dano = 10
        self.image = pygame.image.load('Assets/fire.png').convert_alpha()
        self.rotate()

        self.life_time = 30
            
    def update(self):
        self.move()

        collisions = pygame.sprite.spritecollide(self,self.game.enemy_group, False)
        
        for enemy in collisions:
            if enemy not in self.hit_list:
                enemy.hp -= self.dano
                enemy.on_fire = True               
                self.pierce -= 1
                self.hit_list.append(enemy)
            
            if self.pierce <= 0:
                self.kill()

        self.life_time -= 1
        if self.life_time <= 0:
            self.kill()


        
