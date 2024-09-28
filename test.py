import pygame
import time

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
iImage = 0 #compteur d'images
listColor = [(255,255,255), "yellow", 'pink',"purple", "blue", "red"]
while running:
    iImage += 1
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    # animation de couleur
    screen.fill( (iImage %256, # rouge
                  (2.5*iImage+70) %256, # vert
                 0.8*iImage %256)# bleu
                )#en une ligne !
    # RENDER YOUR GAME HERE
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(50)  # limits FPS to 60

pygame.quit()