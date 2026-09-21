import math

import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
middle = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
circ_y = middle.x + 100
circ_x = middle.y
curr_dir_x = 1
curr_dir_y = 1
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    if running == False:
        screen.fill("red")

    circ_x += 2.5 * curr_dir_x
    if circ_x >= screen.get_width() or circ_x <= 0:
        curr_dir_x *= -1

    circ_y += 5 * curr_dir_y
    if circ_y >= screen.get_height() or circ_y <= 0:
        curr_dir_y *= -1

    pg.draw.circle(screen, "black", (circ_x, circ_y), 5)


    pg.display.flip()
    clock.tick(60)


pg.quit()
