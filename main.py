import pygame
from pygame.locals import *
from menu import MenuScreen, PauseScreen


#set window size
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

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
main_menu = MenuScreen(WINDOW_WIDTH, WINDOW_HEIGHT)
pause_menu = PauseScreen(WINDOW_WIDTH, WINDOW_HEIGHT)

#set variables
show_menu = True
paused = False
game_over = False
fade_counter = 0
FPS = 60


def load_img(file_name):
   try:
      img = pygame.image.load(f"assets/{file_name}")
   except pygame.error as message:
      print(f"Cannot load image: {file_name}")
      raise SystemExit(message)
   img = img.convert_alpha()
   return img

def input(events):
   global running, show_menu, paused, game_over
   for event in events:
      if event.type == pygame.QUIT:
         sys.exit(0)
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            show_menu = False
         if event.key == pygame.K_q:
            running = False
         if not game_over and not show_menu:
            if event.key == pygame.K_p:
                  paused = not paused
         if paused:
            if event.key == pygame.K_m:
               show_menu = True
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
   

#function for drawing background
def draw_bg(bg_img):
   screen.blit(bg_img, (0, 0))
   
   
while running:
   
   clock.tick(FPS)
   input(pygame.event.get())
            
   screen.fill((0, 0, 0))
    
   # Show menu if necessary
   if show_menu:
      main_menu.display_menu()
   elif paused:
      pause_menu.display_menu(screen)
      
   else:
      if not paused:
         if game_over == False:
            #game loop here
            draw_text('Game here', pixel_small, WHITE, 20, 20)
      else:
         #draw pause menu if paused
         pause_menu.display_menu(screen)
   
   #update display
   pygame.display.flip()
    
   
    
pygame.quit()
