import pygame
from random import randint
pygame.init()

window_h=600
window_w=650

win = pygame.display.set_mode((window_h,window_w))
pygame.display.set_caption("Sorting Algorithm Visualizer")

mouse_pos = pygame.mouse.get_pos()

def main():
    while True:

        pygame.time.delay(50)
        pygame.display.update()
        win.fill((0,0,0))
        MENU_TEXT = fonte(50).render("Jogo da veia", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))
        win.blit(MENU_TEXT, MENU_RECT)
        ase = fonte(15).render("Against the machine", True, "grey")
        aere = MENU_TEXT.get_rect(center=(430, 160))
        win.blit(ase, aere)
        pygame.draw.rect(win, (20,50,65), (150,300,300,90))
        ase = fonte(14).render("clique aqui para iniciar", True, "grey")
        aere = MENU_TEXT.get_rect(center=(422, 360))
        win.blit(ase, aere)


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: return 0
            if event.type == pygame.QUIT:pygame.quit()

main()