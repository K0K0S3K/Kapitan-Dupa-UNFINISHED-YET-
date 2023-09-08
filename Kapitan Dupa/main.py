import pygame
import random

from things import *

pygame.init()

font = pygame.font.SysFont('Corbel',28)

def draw_food(screen,color,x,y,radius):
    pygame.draw.circle(screen,color,(x,y),radius)

def init():
    pygame.init()
    pygame.display.set_caption("KAPITAN DUPA")
    pygame.display.set_icon(pygame.image.load('PNG_FILES/logo.png'))
    random.seed(2137)

def starting_screen():
    screen.fill((8,8,8))

    global start
    start = True
    

    screen.blit(NAPIS, (10,10))
    
    for i in range(120):
        draw_food(screen,(255,255,255),random.randint(0,WIDTH),random.randint(0,HEIGHT),1)

    screen.blit(KAPITAN, (700,150))
    screen.blit(PEDAL_7, (420,380))

    pygame.draw.rect(screen,(96,96,96),[START_BUTTON_X,START_BUTTON_Y,BTN_WIDTH,BTN_HEIGHT])
    screen.blit(font.render('START GRY', True , (51,255,51)) , (START_BUTTON_X + 55,START_BUTTON_Y + 10))
    pygame.draw.rect(screen,(96,96,96),[AUTHORS_BUTTON_X,AUTHORS_BUTTON_Y,BTN_WIDTH,BTN_HEIGHT])
    screen.blit(font.render('AUTORZY', True, (51,255,51)), (AUTHORS_BUTTON_X + 60, AUTHORS_BUTTON_Y + 10))
    
    pygame.display.flip()

def starting_buttons(mouse_pos):
    if START_BUTTON_X <= mouse_pos[0] <= START_BUTTON_X + BTN_WIDTH and START_BUTTON_Y <= mouse_pos[1] <= START_BUTTON_Y + BTN_HEIGHT:
        game_init()
        print("btn")
    elif AUTHORS_BUTTON_X <= mouse_pos[0] <= AUTHORS_BUTTON_X + BTN_WIDTH and AUTHORS_BUTTON_Y <= mouse_pos[1] <= AUTHORS_BUTTON_Y + BTN_HEIGHT:
        pygame.quit()
        

def game_init():
    screen.fill((8,8,8))
    global start
    start = False
    global game
    game = True

    screen.blit(BUTTON, (65,550))
    screen.blit(pygame.font.SysFont('Corbel',45).render('SCORE', True, (51,255,51)), (80,565))
    screen.blit(LONG_BUTTON, (260,550) )
    
    screen.blit(BUTTON, (750,550))
    screen.blit(pygame.font.SysFont('Corbel',45).render('SHOT', True, (51,255,51)), (790,585)) 



def main():
    init()
    
    running = True

    starting_screen()

    while running:
        
        mouse_pos = pygame.mouse.get_pos()
        #print(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start:
                    starting_buttons(mouse_pos)
            
            
                print('HUJ')
            
            

            
            
                

        pygame.display.flip()

                

    pygame.quit()



main()




