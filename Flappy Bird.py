#Importing Tools
import pygame
from pygame.locals import *

#Initializing Game
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

#Game Variables
ground_scroll = 0
scroll_speed = 4

#Game's Display Background
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
bg = pygame.image.load('Images_Game_Content/bg.png')
ground_img = pygame.image.load('Images_Game_Content/ground.png')
run = True
while run:

    clock.tick(fps)

    screen.blit(bg, (0, 0))
    screen.blit(ground_img, (ground_scroll, 768 ))
    ground_scroll -= scroll_speed
    # We write the code to resets the background to make it look like it loops
    if abs(ground_scroll) > 30:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()