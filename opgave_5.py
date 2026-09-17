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

    screen.fill("white")
    if running == False:
        screen.fill("red")
    pos = 0
    size = 1
    for x in range(30):
        pg.draw.rect(screen, "black", (pos,pos,size,size))
        pos = size + pos
        size = x * 2


    pg.display.flip()
    clock.tick(60)


pg.quit()
