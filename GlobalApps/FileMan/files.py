import pygame
import PIOS
pygame.init()
window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Files")
running = True
while running:
    window.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PIOS.returncontrol()
            running = False
    pygame.display.flip()