import pygame

pygame.init();
windows = pygame.display.set_mode((800, 600));
while True:
    # Check events: https://www.pygame.org/docs/ref/event.html
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); # Fecha a janela.
            quit(); # Fecha o pygame.

