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
circ_rad = 5
musen = pg.mouse
display_list = []
circ_color = "black"

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    if running == False:
        screen.fill("red")


    if musen.get_pressed(num_buttons=3)[0]:
        display_list.append(musen.get_pos())

    if musen.get_pressed(num_buttons=3)[2]:
        display_list.clear()
    if len(display_list) > 2:
        pg.draw.lines(screen,"black", False, display_list, width=2)



    pg.display.flip()
    clock.tick(60)


pg.quit()
