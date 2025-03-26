import pygame
from enemy import Enemy

def main():
    pygame.init()
    screen = pygame.display.set_mode([1080, 720])

    # criar ponteiro do mouse
    system = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_NO)

    # load images
    enemy_img = pygame.image.load('Projeto_IP/Images/inimigo1.png.webp').convert_alpha()
    background = pygame.image.load('Projeto_IP/Images/pathtd.png').convert_alpha()

    # Settando o background
    def background_img(img):
        tamanho = pygame.transform.scale(img, (1080, 720))
        screen.blit(tamanho, (0, 0))

    # Pathing inicial do inimigo
    waypoint = [(0,380), (185, 380), (185, 170)]
    enemy = Enemy(waypoint, enemy_img)

    # Criando um grupo para armazenar tds os inimigos
    enemy_group = pygame.sprite.Group()
    enemy_group.add(enemy)

    # criar bitmap cursors
    sprite_cursor = pygame.cursors.Cursor(*pygame.cursors.arrow)
    pygame.mouse.set_cursor(sprite_cursor)


    # criar clock do jogo
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        screen.fill((0, 255, 0))
        background_img(background)

        # Executando o Pathing do inimigo
        pygame.draw.lines(screen, 'white', False, waypoint)

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