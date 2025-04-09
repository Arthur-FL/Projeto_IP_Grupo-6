import pygame
from pygame.math import Vector2
from enemy import *
from projectiles import *

class defense(pygame.sprite.Sprite):

        def __init__(self, game, pos):

                self.game = game
                self.groups = self.game.all_sprites_group, self.game.defense_group
                pygame.sprite.Sprite.__init__(self, self.groups)


                #sprite
                #animação
                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                self.animation_delay = 100

                self.image = self.animation_list[self.frame_index]
                self.pos = Vector2(pos)
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
                self.pos[1] += 25
                self.playing_animation = False

                #atributos diferentes nas torres
                self.fire_rate = 1
                self.dano = 1 #dano ou tipo de projetil
                self.range = 1
                self.cost = 0
                
                
                self.cooldown = 1000

        def update(self):


                if self.playing_animation:
                        self.play_animation()
                


                if self.cooldown <= 0:
                        for enemy in self.game.enemy_group:
                        
                                vector = enemy.pos - self.pos
                                dist = vector.length()

                                if dist <= self.range:

                                        self.playing_animation = True


                                        self.shoot(enemy)
                                        self.cooldown = 1000
                                        break
                else:
                        self.cooldown -= self.fire_rate 
        
        def shoot(self, enemy):
                enemy.hp -= self.dano

        def play_animation(self):
                #atualizar imagens
                self.image = self.animation_list[self.frame_index]
                #checa se passou tempo o suficiente desde a ultima atualização
                if pygame.time.get_ticks() - self.update_time > self.animation_delay:
                        self.update_time = pygame.time.get_ticks()
                        self.frame_index += 1
                        #ve se a animação e reseta
                        if self.frame_index >= len(self.animation_list):
                                self.frame_index = 0
                                self.playing_animation = False


        def load_images(self):
                #pega cada imagem da sequencia de imagens
                frame_width = self.sprite_sheet.get_width() // 5 #288
                frame_height = self.sprite_sheet.get_height() # 300
                animation_list = []

                for x in range(5): #quantidade de passos que tem na imagem
                    temp_img = self.sprite_sheet.subsurface((x * frame_width, 0, frame_width, frame_height))
                    animation_list.append(temp_img)

                return animation_list


class def_type1(defense):
        def __init__(self, game, pos):
                super().__init__(game, pos)

                #animação
                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                

                self.image = self.animation_list[self.frame_index] #a imagem dele estatico é o primeiro frame da folha de sprite
                
                self.fire_rate = 18
                self.dano = 25
                self.range = 200
                self.cost = 0
                self.animation_delay = 100

        def shoot(self, enemy):
                arrow(self.game, self.pos, enemy.pos.copy())







class def_type2(defense): # range alto, firerate baixo
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                

                self.image = self.animation_list[self.frame_index]

                self.fire_rate =  10
                self.dano = 100
                self.range = 325
                self.cost = 0

        def shoot(self, enemy):
                snipe(self.game, self.pos, enemy.pos.copy())
        
class def_type3(defense): # range baixo, dps alto 
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                

                self.image = self.animation_list[self.frame_index]

                self.fire_rate = 90
                self.dano = 25
                self.range = 125
                self.cost = 0
        def shoot(self, enemy):
                slash(self.game, self.pos, enemy.pos.copy())

class def_type4(defense): # empurra os inimigos :O
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                

                self.image = self.animation_list[self.frame_index]

                self.fire_rate = 3
                self.dano = 10
                self.range = 160
                self.cost = 0

                
        def shoot(self,enemy):
                push_shot(self.game, self.pos, enemy.pos.copy())


   

 
class def_type5(defense): # taca fogo nos inimigos sla
        def __init__(self, game, pos):
                super().__init__(game, pos)

                self.sprite_sheet = pygame.image.load('Assets/raposa_esquerda1.png').convert_alpha()
                self.animation_list = self.load_images()
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()
                

                self.image = self.animation_list[self.frame_index]

                self.fire_rate = 10
                self.dano = 0
                self.range = 150
                self.cost = 0

        def shoot(self,enemy):
                fire_shot(self.game, self.pos, enemy.pos.copy())







              