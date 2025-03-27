import pygame
from enemy import *
from mapa import * 
def main():
    pygame.init()
    screen = pygame.display.set_mode([1080, 720])

    # criar ponteiro do mouse
    system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO)

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

    
    # criar bitmap cursors
    sprite_cursor = pygame.cursors.Cursor(*pygame.cursors.arrow)
    pygame.mouse.set_cursor(sprite_cursor)


    # criar clock do jogo
    clock = pygame.time.Clock()
    running = True
    paused = False
    while running:
        clock.tick(60)
        screen.fill((0, 255, 0))
        background_img(mapa.imagem)
        
        for event in pygame.event.get():
           #fecha o jogo
            if event.type == pygame.QUIT:
                running = False
            
           # pausa/despausa com ESC 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = not paused
       
        #pygame.draw.lines(screen, 'white', False, waypoints) #--> faz o caminho visível

        if paused:
            #botar uma tela de pause 
            pygame.draw.rect(screen, 'white', (470, 300, 30, 100))
            pygame.draw.rect(screen, 'white', (520, 300, 30, 100))

            






            
        else: # enquando o jogo não estar pausado
            
            #atualiza os inimigos
            enemy_group.update()
        
        

        enemy_group.draw(screen)
        pygame.display.flip()
      
        

        
    pygame.quit()

main()