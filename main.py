import pygame
from random import randint
pygame.init()

window_h=800
window_w=800
list = []
win = pygame.display.set_mode((window_h,window_w))
pygame.display.set_caption("Sorting Algorithm Visualizer")

mouse_pos = pygame.mouse.get_pos()

class settings:
    sound = True
    speed = 50
    array_size= 50

class sort:
    def randomize():
        global list
        list = [0] * settings.array_size
        for i in range(settings.array_size):
            list[i] = randint(5,475)

    def bubble_sort():
        global list
        while True:
            pygame.time.delay(settings.speed)
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
                    plot_screen()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 0
                if event.type == pygame.QUIT:pygame.quit()
    def selection_sort():
        2

    def merge_sort():
        2

    def quick_sort():
        2

    def insertion_sort():
        4

def plot_screen():
    global settings
    win.fill((0,0,0))
    pygame.draw.rect(win, (30,33,32), (0,0,window_w,80))
    MENU_TEXT = fonte(40).render("Sorting Algorithm Visualizer", True, (235,235,245))
    MENU_RECT = MENU_TEXT.get_rect(center=(window_w/2,40))
    win.blit(MENU_TEXT, MENU_RECT)
    pygame.draw.rect(win, (220,180,245), (20+(0*window_w/4),90,160,60))
    pygame.draw.rect(win, (200,200,225), (20+(1*window_w/4),90,160,60))
    pygame.draw.rect(win, (200,200,225), (20+(2*window_w/4),90,160,60))
    pygame.draw.rect(win, (200,200,225), (20+(3*window_w/4),90,160,60))
    pygame.draw.rect(win, (200,200,225), (20+(0*window_w/4),160,160,60))
    pygame.draw.rect(win, (200,200,225), (20+(1*window_w/4),160,160,60))
    opt_txt = fonte(25).render("Reset/randomize", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(100,120))
    win.blit(opt_txt, rect_txt)
    opt_txt = fonte(25).render("Bubble sort", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(300,120))
    win.blit(opt_txt, rect_txt)
    opt_txt = fonte(25).render("Selection sort", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(500,120))
    win.blit(opt_txt, rect_txt)
    opt_txt = fonte(25).render("Merge sort", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(700,120))
    win.blit(opt_txt, rect_txt)
    opt_txt = fonte(25).render("Quick sort", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(100,190))
    win.blit(opt_txt, rect_txt)
    opt_txt = fonte(25).render("Insertion sort", True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(300,190))
    win.blit(opt_txt, rect_txt)
    pygame.draw.rect(win, (20,20,20), (20,300,760,480))

    pygame.draw.rect(win, (137,177,177), (20+(3*window_w/4),160,160,60))
    opt_txt = fonte(25).render(("Speed: "+str(settings.speed)), True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(700,190))
    win.blit(opt_txt, rect_txt)

    if settings.sound == True:
        pygame.draw.rect(win, (20,180,20), (20+(2*window_w/4),160,160,60))
        opt_txt = fonte(25).render("Sound: ON", True, (0,0,0))
        rect_txt = opt_txt.get_rect(center=(500,190))
        win.blit(opt_txt, rect_txt)
    else:
        pygame.draw.rect(win, (180,20,20), (20+(2*window_w/4),160,160,60))
        opt_txt = fonte(25).render("Sound: OFF", True, (0,0,0))
        rect_txt = opt_txt.get_rect(center=(500,190))
        win.blit(opt_txt, rect_txt)

    for i in range(len(list)):
        pygame.draw.rect(win, (200,200,200), (25+(i*750/len(list)), 778-list[i], (750/len(list))-1, list[i]))

    pygame.display.update()

def fonte(size):
    return pygame.font.Font("assets/kenyan coffee rg.ttf", size)

sort.randomize()

while True:
    pygame.time.delay(50)
    plot_screen()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if int(event.pos[0]//200) == 0 and int(event.pos[1]//80) == 1:
                sort.randomize()
            if int(event.pos[0]//200) == 1 and int(event.pos[1]//80) == 1:
                sort.bubble_sort()
            if int(event.pos[0]//200) == 2 and int(event.pos[1]//80) == 1:
                sort.selection_sort()
            if int(event.pos[0]//200) == 3 and int(event.pos[1]//80) == 1:
                sort.merge_sort()
            if int(event.pos[0]//200) == 0 and int(event.pos[1]//80) == 2:
                sort.quick_sort()
            if int(event.pos[0]//200) == 1 and int(event.pos[1]//80) == 2:
                sort.insertion_sort()
            if int(event.pos[0]//200) == 2 and int(event.pos[1]//80) == 2:
                settings.sound = not settings.sound
            if int(event.pos[0]//200) == 3 and int(event.pos[1]//80) == 2:
                if settings.speed == 50:
                    settings.speed = 150
                elif settings.speed == 150:
                    settings.speed = 50
        if event.type == pygame.QUIT:pygame.quit()
