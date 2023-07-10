import pygame

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Solitude")
clock = pygame.time.Clock()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
