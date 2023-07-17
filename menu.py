import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

#create menu screen
class MenuScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def display_menu(self):
        # Set up font
        title_font = pygame.font.SysFont('Pixeloid Sans', 40)
        option_font = pygame.font.SysFont('Pixeloid Sans', 20)

        # Create title text and position on screen
        title_text = title_font.render("Solitude", False, (255, 255, 255))
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (self.width // 2, self.height // 4)

        # Create options and position on screen
        option1_text = option_font.render("Press SPACE to Play", False, (255, 255, 255))
        option1_text_rect = option1_text.get_rect()
        option1_text_rect.center = (self.width // 2, self.height // 2)

        option2_text = option_font.render("Press Q to Quit", False, (255, 255, 255))
        option2_text_rect = option2_text.get_rect()
        option2_text_rect.center = (self.width // 2, self.height * 3 // 4)

        # Draw everything on the screen
        self.screen.fill((0, 0, 0))
        self.screen.blit(title_text, title_text_rect)
        self.screen.blit(option1_text, option1_text_rect)
        self.screen.blit(option2_text, option2_text_rect)
        pygame.display.update()

#create pause screen
class PauseScreen():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont('Pixeloid Sans', 20)
        self.title_text = self.font.render('PAUSED', False, (255, 255, 255))
        self.resume_text = self.font.render("Press 'P' to resume", False, (255, 255, 255))
        self.quit_text = self.font.render("Press 'Q' to quit", False, (255, 255, 255))
        self.mainmenu_text = self.font.render("Press 'M' to return to Main Menu", False, (255, 255, 255))

    def display_menu(self, screen):
        # Draw a transparent overlay to make the game appear paused
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Draw the pause menu text
        screen.blit(self.title_text, (self.screen_width//2 - self.title_text.get_width()//2, self.screen_height//3))
        screen.blit(self.resume_text, (self.screen_width//2 - self.resume_text.get_width()//2, self.screen_height//2))
        screen.blit(self.quit_text, (self.screen_width//2 - self.quit_text.get_width()//2, self.screen_height//2 + 50))
        screen.blit(self.mainmenu_text, (self.screen_width//2 - self.mainmenu_text.get_width()//2, self.screen_height//2 + 100))
