import math

import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((2,48,32))
    if running == False:
        screen.fill("red")

    for x in range(8):
        for y in range(8):
            color = (((x+y)%2*255), ((x+y)%2*255), ((x+y)%2)*255)
            x_pos = 25+(x*25)
            y_pos = 25+(y*25)
            pg.draw.rect(screen, color, (x_pos, y_pos, 25,25))


    pg.display.flip()
    clock.tick(60)


pg.quit()

