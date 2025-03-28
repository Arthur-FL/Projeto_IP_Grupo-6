import pygame
from enemy import *
from mapa import * 
import random
from health_drop import *


random.randint(1,3) #pro tempo
random.randint(1,3) # pro local


def main():
    pygame.init()
    screen = pygame.display.set_mode([1080, 720])
    fonte = pygame.font.SysFont('Arial', 55)
    
    # Settando o background
    
    mapa = map()
    def background_img(img):
        tamanho = pygame.transform.scale(img, (1080, 720))
        screen.blit(tamanho, (0, 0))

    # Pathing inicial do inimigo
    waypoints = mapa.waypoints
    enemy1 = enem_type1()
    enemy2 = enem_type2()
    enemy3 = enem_type3()
    # Criando um grupo para armazenar tds os inimigos
    enemy_group = pygame.sprite.Group()
    enemy_group.add(enemy1)
    enemy_group.add(enemy2)
    enemy_group.add(enemy3)

    #
    collectables_group = pygame.sprite.Group()

    # criar bitmap cursors
    sprite_cursor = pygame.cursors.Cursor(*pygame.cursors.arrow)
    pygame.mouse.set_cursor(sprite_cursor)

    # criar clock do jogo
    clock = pygame.time.Clock()
    running = True
    paused = False
    
    # vida é 10 ^^ 
    vida = 10
    morto = False # quer dizer q n ta vivo :)

    # coração <3

    timer_coracao = random.randint(60,360)


    # JOGO
    while running:
        clock.tick(60)
        screen.fill((0, 255, 0))
        background_img(mapa.imagem)
        
        #TU MORREU
        if vida == 0:
            morto = True

        for event in pygame.event.get():
           #fecha o jogo
            if event.type == pygame.QUIT:
                running = False
           # pausa/despausa com ESC 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused
        
        if paused:
            #botar uma tela de pause 
            pygame.draw.rect(screen, 'white', (470, 300, 30, 100))
            pygame.draw.rect(screen, 'white', (520, 300, 30, 100))

          
        elif not morto: # enquando o jogo não esta pausado
            
            # coração
            if timer_coracao == 0:
                timer_coracao = random.randint(60,360)
                posicao = (random.randint(100,500),random.randint(100,500))
                
                hp = health_drop(posicao)
                collectables_group.add(hp)

            else:
                timer_coracao -=1

            #atualiza os inimigos
            enemy_group.update()
            
            for enemy in enemy_group:
                if enemy.final:
                    enemy_group.remove(enemy)
                    vida -=1



        # printar a vida
        screen.blit(fonte.render(str(vida), True, (255, 255, 255)), (1000, 0))
        screen.blit(pygame.image.load('Assets/heart.png').convert_alpha(), (940,7))
        enemy_group.draw(screen)
        collectables_group.draw(screen)
        
        
        # printar a tela de game over quando o cara morre
        if morto:
            screen.blit(pygame.image.load('Assets/game_over.png').convert_alpha(),(0,0))
        
        
        



        #pygame.draw.lines(screen, 'white', False, waypoints) #--> faz o caminho visível
        
        #flipa a tela
        pygame.display.flip()
       
    pygame.quit()

main()