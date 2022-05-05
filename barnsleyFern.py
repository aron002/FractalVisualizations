import pygame
from random import randint


def mutant_fern(x, y):
    number = randint(1,100)
    if number == 1:
        return 0, 0.25 * y - 0.4
    elif number <= 86:
        return 0.95 * x + 0.005 * y - 0.002, -0.005 * x + 0.93 * y + 0.5
    elif number <= 93:
        return 0.035 * x - 0.2 * y - 0.09, 0.16 * x + 0.04 * y + 0.02
    else:
        return -0.04 * x + 0.2 * y + 0.083, 0.16 * x + 0.04 * y + 0.12


def fern(x, y):
    number = randint(1,100)
    if number <= 2:
        return 0, 0.16 * y
    elif number <= 86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif number <= 93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44


def draw():
    stop = False
    prevX, prevY = 0, 0

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
        X, Y = fern(prevX, prevY)
        pygame.draw.circle(gameDisplay, (0, 255, 0), transform(X, Y), 1)
        prevX, prevY = X, Y
        pygame.display.update()    
    pygame.quit()
    

def transform(x, y):
    return x*XSCALE+400, y*YSCALE
        

if __name__ == '__main__':
    XSCALE, YSCALE = 80, 60
    WIDTH, HEIGHT = 800, 600

    pygame.init()
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Barnsley's Fern")
    draw()
    
