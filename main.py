import pygame
from pygame.locals import *
from menu import CreateMenu


#set window size
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 720

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Solitude")
clock = pygame.time.Clock()
running = True

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL = (48, 96, 130)

#define fonts
pixel_small = pygame.font.SysFont('Pixeloid Sans', 20)
pixel_large = pygame.font.SysFont('Pixeloid Sans', 24)

#initialize menu
main_menu = CreateMenu(WINDOW_WIDTH, WINDOW_HEIGHT, "Solitude", ["Play Game", "Options", "Q to Quit"])


def input(events):
   for event in events:
      if event.type == pygame.QUIT:
         sys.exit(0)
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_q:
            sys.exit(0)
         elif event.key == pygame.K_p:
            #pause the game
            pass
         #check player choice
         elif event.key == pygame.K_w:
            pass
         elif event.key == pygame.K_a:
            pass
         elif event.key == pygame.K_s:
            pass
         elif event.key == pygame.K_d:
            pass
         #check items
         elif event.key == pygame.K_i:
            pass
             
      

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
   img = font.render(text, False, text_col)
   screen.blit(img, (x, y))

while running:
    
   input(pygame.event.get())
            
   screen.fill((0, 0, 0))
    
   #draw_text('Solitude', pixel_large, WHITE, WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 100)
   #display menu
   main_menu.display_menu()
    
   pygame.display.flip()
    
   clock.tick(60)
    
pygame.quit()
