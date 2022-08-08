import numpy
import pygame
from random import randint
pygame.init()

window_h=800
window_w=800
list = []
last_swapped = []
win = pygame.display.set_mode((window_h,window_w))
pygame.display.set_caption("Sorting Algorithm Visualizer")

mouse_pos = pygame.mouse.get_pos()

class settings:
    sound = False
    speed = 30
    array_shown = 250
    array_size = int(array_shown/2)+1

class sort:

    def check():
        global last_swapped
        for k in range(len(list)-1):
            if list[k] > list[k+1]:
                return 0
        last_swapped = []
        return True

    def randomize():
        global list
        list = [0] * settings.array_size
        for i in range(settings.array_size):
            list[i] = randint(5,475)

    def bubble_sort():
        global last_swapped
        while True:
            verify = sort.check()
            if verify: return 0
            pygame.time.delay(settings.speed)
            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
                    last_swapped = [i,i+1]
                    sound(list[i])
                    plot_screen()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 0
                if event.type == pygame.QUIT:pygame.quit()

    def selection_sort():
        global last_swapped
        for i in range(len(list)):
            pygame.time.delay(settings.speed)
            min = i

            for j in range(i+1,len(list)):
                if list[j] < list[min]:
                    min = j

            if list[i] != list[min]:
                aux = list[i]
                list[i] = list[min]
                list[min] = aux
                last_swapped = [i,min]
                sound(list[i])
                plot_screen()
        verify = sort.check()
        if verify: return 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:pygame.quit()

    def merge(l, m, r):
        global last_swapped
        pygame.time.delay(settings.speed)
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = list[l + i]

        for j in range(0, n2):
            R[j] = list[m + 1 + j]
    
        i = 0
        j = 0
        k = l
        last_swapped = [k]
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            list[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            list[k] = R[j]
            j += 1
            k += 1

        plot_screen()
        verify = sort.check()
        if verify: return 0
    
    def merge_sort(l, r):
        if l < r:

            m = l+(r-l)//2
    
            sort.merge_sort(l, m)
            sort.merge_sort(m+1, r)
            sort.merge(l, m, r)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:pygame.quit()
        
    def quick_sort():
        global last_swapped
        pygame.time.delay(settings.speed)
        last_swapped = [i,i+1]
        sound(list[i])
        plot_screen()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return 0
            if event.type == pygame.QUIT:pygame.quit()

    def insertion_sort():
        global last_swapped
        for i in range(len(list)-1):
            key = list[i]
            j = i
                
            while j >= 0 and key < list[j]:
                list[j + 1] = list[j]
                j = j - 1

            list[j + 1] = key
            last_swapped = [j+1]
            plot_screen()

def sound(freq):
    if settings.sound == True:
        sampleRate = 44100
        freq = 200+5*freq
        pygame.mixer.init(44100,-16,2,512)
        arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        arr2 = numpy.c_[arr,arr]
        sound = pygame.sndarray.make_sound(arr2)
        sound.play(-1)
        pygame.time.delay(50)
        sound.stop()

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
    if settings.speed == 120: speed_status = 'slow'
    elif settings.speed == 30: speed_status = 'medium'
    elif settings.speed == 0: speed_status = 'fast'
    opt_txt = fonte(25).render(("Speed: "+speed_status), True, (0,0,0))
    rect_txt = opt_txt.get_rect(center=(700,190))
    win.blit(opt_txt, rect_txt)

    if settings.sound == True:
        pygame.draw.rect(win, (20,180,20), (20+(2*window_w/4),160,160,60))
        opt_txt = fonte(25).render("Sound: ON (slower)", True, (0,0,0))
        rect_txt = opt_txt.get_rect(center=(500,190))
        win.blit(opt_txt, rect_txt)
    else:
        pygame.draw.rect(win, (180,20,20), (20+(2*window_w/4),160,160,60))
        opt_txt = fonte(25).render("Sound: OFF (faster)", True, (0,0,0))
        rect_txt = opt_txt.get_rect(center=(500,190))
        win.blit(opt_txt, rect_txt)
    
    opt_txt = fonte(28).render(("Array size:   "+str(int(settings.array_size))), True, (235,235,245))
    rect_txt = opt_txt.get_rect(center=(100,260))
    win.blit(opt_txt, rect_txt)

    '''for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(win, (137,177,177), (250,260,500,4))
            pygame.draw.circle(win,(137,177,177),(event.pos[0],262),12)
            pygame.draw.circle(win,(70,105,90),(event.pos[0],262),8)
        else: '''
    pygame.draw.rect(win, (137,177,177), (250,260,500,4))
    pygame.draw.circle(win,(137,177,177),(250+(settings.array_shown),262),12)
    pygame.draw.circle(win,(70,105,90),(250+(settings.array_shown),262),8)


    for i in range(len(list)):
        pygame.draw.rect(win, (200,200,200), (25+(i*750/len(list)), 778-list[i], (750/len(list))-1, list[i]))
    for i in range(len(last_swapped)):
        pygame.draw.rect(win, (255,50,50), (25+(last_swapped[i]*750/len(list)), 778-list[last_swapped[i]], (750/len(list))-1, list[last_swapped[i]]))

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
                sort.merge_sort(0,len(list)-1)
            if int(event.pos[0]//200) == 0 and int(event.pos[1]//80) == 2:
                sort.quick_sort()
            if int(event.pos[0]//200) == 1 and int(event.pos[1]//80) == 2:
                sort.insertion_sort()
            if int(event.pos[0]//200) == 2 and int(event.pos[1]//80) == 2:
                settings.sound = not settings.sound
            if int(event.pos[0]//200) == 3 and int(event.pos[1]//80) == 2:
                if settings.speed == 120:
                    settings.speed = 30
                elif settings.speed == 30:
                    settings.speed = 0
                elif settings.speed == 0:
                    settings.speed = 120
        
        if pygame.mouse.get_pressed()[0]:
            try:
                if int(event.pos[1]//80) == 3 and event.pos[0] > 250 and event.pos[0] < 750:
                    settings.array_shown = event.pos[0] - 250
                    settings.array_size = int((settings.array_shown)/2)+1
                    sort.randomize()
            except: pass
        if event.type == pygame.QUIT:pygame.quit()