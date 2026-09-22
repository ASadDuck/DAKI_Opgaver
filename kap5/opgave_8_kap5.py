import math
from random import randint

import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
middle = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
circ_rad = 50
musen = pg.mouse
display_list = []
circ_color = "black"
cooldown = 100
last = pg.time.get_ticks()
circ_ligning = circ_rad + 1
poly_list = []
color_list = []


while running:
    now = pg.time.get_ticks()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    if running == False:
        screen.fill("red")


    if musen.get_pressed(num_buttons=3)[0] and now - last >= cooldown:
        display_list.append(musen.get_pos())
        last = pg.time.get_ticks()

    if musen.get_pressed(num_buttons=3)[2]:
        display_list.clear()

    if len(poly_list) >= 1:
        for x, points in enumerate(poly_list):
            pg.draw.polygon(screen, color_list[x], points)


    if len(display_list) >= 2:
        pg.draw.lines(screen,"black", False, display_list, width=2)
        circ_ligning = (math.pow((display_list[-1][0] - display_list[0][0]), 2) +
                        math.pow((display_list[-1][1] - display_list[0][1]), 2))


    if circ_ligning <= circ_rad:
        if len(display_list) == 2:
            continue
        display_list.pop()
        display_list.append(display_list[0])
        poly_list.append(display_list.copy())
        display_list.clear()
        circ_ligning = circ_rad + 1
        color_list.append((randint(0, 255), randint(0, 255), randint(0, 255)))


    pg.display.flip()
    clock.tick(60)


pg.quit()
