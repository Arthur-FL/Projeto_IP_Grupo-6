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
        tamanho = pygame.transform.scale(mapa.imagem, (1080, 720))
        screen.blit(tamanho, (0, 0))

    # Pathing inicial do inimigo
    waypoints = mapa.waypoints
    enemy = Enemy(waypoints)

    # fiz um inimigo 2 :D
    enemy2 = Enemy(waypoints)
    enemy2.speed = 5
    # Criando um grupo para armazenar tds os inimigos
    enemy_group = pygame.sprite.Group()
    enemy_group.add(enemy)
    enemy_group.add(enemy2)



    # criar bitmap cursors
    sprite_cursor = pygame.cursors.Cursor(*pygame.cursors.arrow)
    pygame.mouse.set_cursor(sprite_cursor)


    # criar clock do jogo
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 255, 0))
        background_img(mapa.imagem)

       
        # pygame.draw.lines(screen, 'white', False, waypoints) --> faz o caminho visível

        # Atualizar e printar o inimigo na tela
        enemy_group.update()
        enemy_group.draw(screen)
        pygame.display.flip()
        # terminar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
    pygame.quit()

main()