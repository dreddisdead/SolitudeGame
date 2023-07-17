import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

class CreateMenu:
    def __init__(self, width, height, title=None, options=[]):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.options = options
        
    def display_menu(self):
        #set up fonts
        title_font = pygame.font.SysFont('Pixeloid Sans', 40)
        option_font = pygame.font.SysFont('Pixeloid Sans', 20)
        
        # Create title text and position on screen
        if self.title != None:
            title_text = title_font.render(self.title, False, (255, 255, 255))
        else:
            title_text = title_font.render("", False, (255, 255, 255))
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (self.width // 2, self.height // 4)
        
        # Create options and position on screen
        option1_text = option_font.render(self.options[0], False, (255, 255, 255))
        option1_text_rect = option1_text.get_rect()
        option1_text_rect.center = (self.width // 2, self.height // 2)

        option2_text = option_font.render(self.options[1], False, (255, 255, 255))
        option2_text_rect = option2_text.get_rect()
        option2_text_rect.center = (self.width // 2, self.height // 2 + 50)
        
        option3_text = option_font.render(self.options[2], False, (255, 255, 255))
        option3_text_rect = option2_text.get_rect()
        option3_text_rect.center = (self.width // 2, self.height // 2 + 100)
        
        # Draw everything on the screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(title_text, title_text_rect)
        self.screen.blit(option1_text, option1_text_rect)
        self.screen.blit(option2_text, option2_text_rect)
        self.screen.blit(option3_text, option3_text_rect)
        pygame.display.update()
