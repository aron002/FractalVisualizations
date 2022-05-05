import pygame


def draw():
    stop = False
    prevX, prevY = 0, 0
    countWidth = 0
    countHeight = 0

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True
                
        if countHeight <= HEIGHT:
            x0 = 3.5/WIDTH * countWidth - 2.5
            y0 = 2/HEIGHT * countHeight - 1
            x = 0
            y = 0
            i = 0
            maxi = 1000
            while x*x + y*y <= 2.2 and i < maxi:
                xtemp = x*x - y*y + x0
                y = 2*x*y + y0
                x = xtemp
                i += 1
            r, g, b = 255, 255, 255
            if i <= 255:
                r = 255 - i
            elif i <= 510:
                r = 0
                g = 255 - (i - 255)
            elif i <= 765:
                r = 0
                g = 0
                b = 255 - (i  -510)
            else:
                r = g = b = 0
            color = r, g, b
            pygame.draw.rect(gameDisplay, color, (countWidth, countHeight, PIXELWIDTH, PIXELHEIGHT))

        if countWidth >= WIDTH:
            countWidth = 0
            countHeight += PIXELHEIGHT
        else:
            countWidth += PIXELWIDTH
            
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    XSCALE, YSCALE = 130, 100
    WIDTH, HEIGHT = 1200, 900
    PIXELWIDTH = PIXELHEIGHT = 10

    pygame.init()
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mandelbrot Set")
    draw()
