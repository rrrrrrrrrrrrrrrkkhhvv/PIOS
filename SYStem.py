import pygame
import pygame.freetype
import os

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((1080, 720))
dir = os.path.dirname(os.path.abspath(__file__))
apps = [["Terminal", "GlobalApps/Terminal/term.py"], ["Files", "GlobalApps/FileMan/files.py"]]
running = True
pygame.display.set_caption("PIOS - Home")

FONT_SISE = 12
font = pygame.freetype.Font("MonospaceTypewriter.ttf", FONT_SISE)

while running:
    dolast = []
    window.fill((0, 0, 0))
    
    c = len(apps) * 95 - 95
    hoverover = ""
    
    for i in apps:
        x, y = pygame.mouse.get_pos()
        tmp = pygame.draw.rect(window, (255, 255, 255), (15 + c, 15, 75, 75))
        if 15 + c < x < 90 + c and 15 < y < 90:
            pygame.draw.rect(window, (255, 255, 255), (x, y - 6, len(i[0]) * FONT_SISE / 1.5, FONT_SISE + 2))
            font.render_to(window, (x + 5, y - 5), i[0], (0, 0, 0))
            hoverover = i[1]
        c = c - 95
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            exec(open(hoverover, 'r').read())
            

    for i in dolast:
        i

    pygame.display.flip()