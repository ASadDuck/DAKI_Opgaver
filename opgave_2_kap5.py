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

    for x in range(360):
        r = 0.1 * x * 5
        angle = math.radians(x * 5)
        pg.draw.rect(screen, "black", (middle.x + r*math.cos(angle), middle.y + r*math.sin(angle), 5, 5))


#    for x in range(360):
#        angle = x*5
#        r = 0.1*angle
#        pg.draw.rect(screen, "black", (middle.x + r*math.cos(angle), middle.y + r*math.sin(angle), 5, 5))



    pg.display.flip()
    clock.tick(60)


pg.quit()
