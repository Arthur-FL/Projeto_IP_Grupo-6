import pygame
from enemy import *
from mapa import *
from health_drop import *
import time
class game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([1080, 720])
        self.fonte = pygame.font.SysFont('Arial', 55)


        self.enemy_group = pygame.sprite.Group()
        self.defense_group = pygame.sprite.Group()
        self.dropped_items_group = pygame.sprite.Group()
        self.projectile_group = pygame.sprite.Group()
        self.HUD_elements_group = pygame.sprite.Group()
        

        self.paused = False
        self.running = False
        self.in_menu = False
        self.in_pause_menu = False
        self.in_wave = False
        self.game_over = False
        self.win = False
        
        self.enemy_group = pygame.sprite.Group()
        self.mapa = map()

        ##
        self.hp = 99
        self.current_wave = 0
        

    def update(self):
        
        if not self.paused:
            
            
            #update dos inimigos
            self.enemy_group.update()
            for enemy in self.enemy_group:
                    if enemy.final:
                        self.enemy_group.remove(enemy)
                        self.hp -= enemy.dano

                    if enemy.morto:
                        self.enemy_group.remove(enemy)
                        coin = enemy.drop()
                        self.dropped_items_group.add(coin)
                        

            if not self.enemy_group:
                    self.in_wave = False
            
            # update das defesas
            self.defense_group.update()
            #update de items no chão
            #coração (?)
            if not self.dropped_items_group:
                self.dropped_items_group.add(health_drop())
            if self.in_wave:
                self.dropped_items_group.update()

                
            # update de projeteis na tela
            self.projectile_group.update()
            # update da HUD
            self.HUD_elements_group.update() # a vida devia estar aqui eu acho


            #player morreu
            if self.hp <= 0:
                self.game_over = True 
       
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
            if not self.paused and not self.in_menu:
                # spawna próxima wave de inimigos
                if command.type == pygame.KEYDOWN and command.key == pygame.K_SPACE and not self.in_wave:
                    self.start_wave(self.current_wave)
                    self.current_wave += 1
                
                # funcionamento e coleta de um item dropado no chão # por enquanto ta coletando a tela toda quando aperta C
                if command.type == pygame.KEYDOWN and command.key == pygame.K_c:
                    
                    self.dropped_items_group = pygame.sprite.Group()
                    self.hp += 1

    def start_wave(self, wave):
        self.in_wave = True
        
        waypoints = self.mapa.waypoints
        new_enemies = self.mapa.waves[wave] # lista com os tipos de inimigos q precisa spawnar na wave 
        
        for enemy_type in new_enemies:
            if enemy_type == 1:
                 enemy = enem_type1(waypoints)
                 self.enemy_group.add(enemy)
            elif enemy_type == 2:
                enemy = enem_type2(waypoints)
                self.enemy_group.add(enemy)
            elif enemy_type == 3:
                enemy = enem_type3(waypoints)
                self.enemy_group.add(enemy)
            
            for _ in range(5):
                self.enemy_group.update()

    def display(self, screen):
        # reset screen
        self.screen.fill((255, 255, 255))
        
        # tela game over
        if self.game_over:
            self.screen.blit(pygame.image.load('Assets/game_over.png').convert_alpha(),(0,0))
        # tela de vitoria
        elif self.win:
            self.screen.blit(pygame.image.load('Assets/game_over.png').convert_alpha(),(0,0)) # ainda ta usando a tela de game over
        else:



            # desenha o jogo quando n ta pausado
            if not self.paused:
                background = pygame.transform.scale(self.mapa.imagem, (1080, 720))
                screen.blit(background, (0, 0))
            
                # desenha os objetos do jogo
                self.enemy_group.draw(screen) 
                self.defense_group.draw(screen)
                self.dropped_items_group.draw(screen)
                self.projectile_group.draw(screen)
                self.HUD_elements_group.draw(screen)
                
                # HUD vida, talves mover isso pra uma classe de HUD (??)
                screen.blit(self.fonte.render(str(self.hp), True, (255, 255, 255)), (980, 0))
                screen.blit(pygame.image.load('Assets/heart.png').convert_alpha(), (920,7))



                # HUD imagem de debug pra ver se tem uma wave ta acontecendo
                if self.in_wave:
                    screen.blit(pygame.image.load('Assets/enemy1.webp').convert_alpha(), (810, 7))

            
            


            # desenha tela de pause
            else:
                tela_pause = pygame.transform.scale(self.mapa.imagem, (1080, 720))
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