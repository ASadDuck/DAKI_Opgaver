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

    middle = pg.Vector2(screen.get_width()/2, screen.get_height()/2)

    for line in range(12):
        pg.draw.line(screen, "black", (middle.x, middle.y),
                     (middle.x + 200 * math.cos(math.radians(line*30)),
                      middle.y + 200 * math.sin(math.radians(line*30))), width=5)


    pg.display.flip()
    clock.tick(60)


pg.quit()

