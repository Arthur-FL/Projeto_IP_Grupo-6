import pygame
from enemy import *
from mapa import *
from random_drops import *

class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1080, 720])
        self.fonte = pygame.font.SysFont('Arial', 55)


        #grupos de sprites usados
        self.enemy_group = pygame.sprite.Group()
        self.defense_group = pygame.sprite.Group()
        self.dropped_items_group = pygame.sprite.Group()
        self.projectile_group = pygame.sprite.Group()
        self.HUD_elements_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.all_sprites_group = pygame.sprite.Group()


        # gerador aleatório de drops no mapa 
        self.item_gen = drop_generator(self)

        # condicionais pro estado atual do jogo
        self.paused = False
        self.running = False
        self.in_wave = False
        self.game_over = False
        self.win = False
        self.debug_view = False

        # variaveis de spawn de inimigos
        self.spawn_cooldown = 500
        self.last_spawn = 0
        self.current_enemies = []
        self.enemy_index = 0
        

        # mapa 
        self.mapa = map()

        ##
        self.hp = 25
        self.money = 5
        self.current_wave = 0
        self.shield = False

        self.player = player(self)



        

    def update(self):
        self.defesas = [str(type(i)) for i in self.defense_group.sprites()]
        self.custos = {1: 5 + 2*self.defesas.count("<class 'defenses.def_type1'>"),
                       2: 9 + 5*self.defesas.count("<class 'defenses.def_type2'>"),
                       3: 10 + 5*self.defesas.count("<class 'defenses.def_type3'>"),
                       4: 7 + 7*self.defesas.count("<class 'defenses.def_type4'>"),
                       5: 12 + 6*self.defesas.count("<class 'defenses.def_type5'>")}
        
        

        if not self.paused:
            
            self.all_sprites_group.update()
            
            if self.enemy_group:
                self.item_gen.update()

            #player morreu
            if self.hp <= 0:
                self.game_over = True 


            # novo spawn das waves
            if self.in_wave:
                if pygame.time.get_ticks() - self.last_spawn > self.spawn_cooldown:

                    enemy_type = self.current_enemies[self.enemy_index]
                    self.last_spawn = pygame.time.get_ticks()
                    self.enemy_index += 1

                    if self.enemy_index >= len(self.current_enemies):
                        self.enemy_index = 0
                        self.in_wave = False
                        
                    if enemy_type == '':
                        pass
                    if enemy_type == 1:
                        enem_type1(self)
                        self.spawn_cooldown = 500                                                               
                        
                    elif enemy_type == 2:
                        enem_type2(self)
                        self.spawn_cooldown = 500
                
                    elif enemy_type == 3:
                        enem_type3(self)
                        self.spawn_cooldown = 100

                    elif enemy_type == 4:
                        enem_type4(self)
                        self.spawn_cooldown = 500

                    elif enemy_type == 5:
                        enem_type5(self)
                        self.spawn_cooldown = 500
       
    def comandos(self):
        
        for command in pygame.event.get():
           
           #comandos globais(funcionam toda hora)

           #fecha o jogo
            if command.type == pygame.QUIT:
                self.running = False
          
           # pausa/despausa (ESC) 
            if command.type == pygame.KEYDOWN and command.key == pygame.K_ESCAPE:
                self.paused = not self.paused



            
            #comandos dentro do jogo(não funcionam se estiver em um menu/jogo pausado)
            if not self.paused:
                # spawna próxima wave de inimigos
                if command.type == pygame.KEYDOWN and command.key == pygame.K_SPACE and not self.in_wave:
                    self.start_wave()

                
                # comandos para colocar defesas
                if command.type == pygame.KEYDOWN and command.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,]:
                    pos = self.player.pos       

                    #verifica se ja existe uma defesa na posição
                    can_place = all(not tower.rect.collidepoint(pos) for tower in self.defense_group)

                    #verifica se ta muito próximo do caminho dos inimigos
                    too_close_to_path = point_near_path(pos, self.mapa.waypoints)

                    if can_place and not too_close_to_path:
                        if command.key == pygame.K_1 and self.money>= self.custos[1]:
                            def_type1(self, pos)
                            self.money -= self.custos[1]
                        elif command.key == pygame.K_2 and self.money>= self.custos[2]:
                            def_type2(self, pos)
                            self.money -= self.custos[1]
                        elif command.key == pygame.K_3 and self.money>= self.custos[3]:
                            def_type3(self, pos)
                            self.money -= self.custos[3]
                        elif command.key == pygame.K_4 and self.money>= self.custos[4]:
                            def_type4(self, pos)
                            self.money -= self.custos[4]
                        elif command.key == pygame.K_5 and self.money>= self.custos[5]:
                            def_type5(self, pos)
                            self.money -= self.custos[5]
                        
                    
             
                if command.type in [pygame.KEYDOWN, pygame.KEYUP] and command.key == pygame.K_TAB:
                    self.debug_view = not self.debug_view
                    
    def start_wave(self):
        self.in_wave = True
        
        
        if self.current_wave < len(self.mapa.waves):
            self.current_enemies =  self.mapa.waves[self.current_wave]
            
            self.current_wave += 1
            
        else:
            self.win = True

    def display(self, screen):
        # reset screen
        self.screen.fill((255, 255, 255))
        
        # tela game over
        if self.game_over:
            self.screen.blit(pygame.image.load('Assets/game_over.png').convert_alpha(),(0,0))
        # tela de vitoria
        elif self.win:
            self.screen.blit(pygame.transform.scale(pygame.image.load('Assets/win_screen.png'), (1080,720)),(0,0))
        else:



            # desenha o jogo quando n ta pausado
            
            background = pygame.transform.scale(self.mapa.imagem, (1080, 720))
            screen.blit(background, (0, 0))
        
            # desenha os objetos do jogo
            self.enemy_group.draw(screen) 
            self.defense_group.draw(screen)
            self.dropped_items_group.draw(screen)
            self.projectile_group.draw(screen)
            self.HUD_elements_group.draw(screen)
            self.player_group.draw(screen)

            # HUD vida, talves mover isso pra uma classe de HUD (??)
            screen.blit(self.fonte.render(str(self.hp), True, (255, 255, 255)), (980, 0))
            screen.blit(pygame.image.load('Assets/heart.png').convert_alpha(), (920,7))
            if self.shield:
                    screen.blit(pygame.transform.scale(pygame.image.load('Assets/shield.png'), (60,60)), (855,0))

            #hud moeda
            screen.blit(self.fonte.render(str(self.money), True, (255, 255, 255)), (980, 50))
            screen.blit( pygame.transform.scale(pygame.image.load('Assets/coin.png'), (50,50)), (920,57))
            #numero de waves
            screen.blit(self.fonte.render(str(self.current_wave), True, (255, 255, 255)), (980, 120))
            screen.blit( pygame.transform.scale(pygame.image.load('Assets/enemy1.png'), (50,50)), (920,127))
            #preços
            screen.blit(self.fonte.render(str(self.custos[1]), True, (255, 255, 255)), (50, 650 ))
            screen.blit(self.fonte.render(str(self.custos[2]), True, (255, 255, 255)), (125, 650 ))
            screen.blit(self.fonte.render(str(self.custos[3]), True, (255, 255, 255)), (200, 650 ))
            screen.blit(self.fonte.render(str(self.custos[4]), True, (255, 255, 255)), (275, 650 ))
            screen.blit(self.fonte.render(str(self.custos[5]), True, (255, 255, 255)), (350, 650 ))



            # debug view
            if self.debug_view:
                # atributos das defesas
                for tower in self.defense_group:
                    pos = tower.pos.copy()
                    pos[0] -= 25
                    pos[1] -= 110
                    pygame.draw.circle(screen, 'black', tower.pos , tower.range - 20, 3)
                    screen.blit(self.fonte.render(str(tower.cooldown), True, (255, 255, 255)), pos)

                # vida dos inimigos
                for enemy in self.enemy_group:
                    pos = enemy.pos.copy()
                    pos[0] -= 25
                    pos[1] -= 110
                    screen.blit(self.fonte.render(str(round(enemy.hp)), True, (255, 255, 255)), pos)

                # caminho 
                pygame.draw.lines(screen, 'white', False, self.mapa.waypoints)

                #fds dos projeteis
                for shot in self.projectile_group:
                    pos = shot.pos.copy()
                    pos[0] -= 25                                                    
                    pos[1] -= 110
                    screen.blit(self.fonte.render(str(shot.pierce), True, (255, 255, 255)), pos)
                       
                        




                #HUD imagem de debug pra ver se tem uma wave ta acontecendo
                #if self.in_wave:
                    #screen.blit(pygame.image.load('Assets/enemy1.webp').convert_alpha(), (810, 7))

            
            


            # desenha tela de pause
            if self.paused:
                tela_pause = pygame.image.load('Assets/pathtd.png').convert_alpha()
                screen.blit(tela_pause, (0, 0))
        
        
        pygame.display.flip()


    def run_game(self):
        self.screen = pygame.display.set_mode([1080, 720])
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)
            
            
            # inputs do usuário
            self.comandos()

            # update geral de todos os objetos do jogo
            self.update()

            # update do display
            self.display(self.screen)

    



        pygame.quit()




if __name__ == '__main__':
    jogo = game()
    jogo.run_game()
