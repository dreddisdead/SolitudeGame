import pygame
from pygame.locals import *
import random
import sys
import time


#All scenes from the game are defined here
class GameScenes:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    
    def display_scene(self, scene):
        self.scene = scene
        pass
    
    #First scene of the game
    def intro_scene(self):
        pass
    #Only playable scene of the game while the functionality of the game is being developed
    def demo_scene(self):
        pass