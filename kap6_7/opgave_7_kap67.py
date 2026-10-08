import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
pg.display.set_caption("Uranium Fever")
running = True
size = pg.Vector2(25,25)
playerpos = pg.Vector2(300,300)
player_speed = 3
curr_dir = pg.Vector2(0,0)
uranium = []
circ_rad = 5


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    while len(uranium) < 10:
        uranium.append(pg.Vector2(random.randint(circ_rad, screen.get_width()-circ_rad),
                                  random.randint(circ_rad, screen.get_height()-circ_rad)))


    keys_pressed = pg.key.get_pressed()

    screen.fill("black")
    if running == False:
        screen.fill("blue")
    last_key = pg.key.get_just_pressed()

    if keys_pressed[pg.K_a] and keys_pressed[pg.K_d]:
        pass
    else:
        if keys_pressed[pg.K_a]:
            curr_dir.x = -1
        if keys_pressed[pg.K_d]:
            curr_dir.x = 1

    if keys_pressed[pg.K_w] and keys_pressed[pg.K_s]:
        pass
    else:
        if keys_pressed[pg.K_w]:
            curr_dir.y = -1
        if keys_pressed[pg.K_s]:
            curr_dir.y = 1

    for uran in uranium:
        pg.draw.circle(screen, "green", uran, circ_rad)

    playerpos.x = (curr_dir.x * player_speed) + playerpos.x
    playerpos.y = (curr_dir.y * player_speed) + playerpos.y
    if playerpos.x > screen.get_width() + (size.x/2): playerpos.x = playerpos.x - screen.get_width() - size.x/2
    if playerpos.x <  -(size.x/2): playerpos.x = playerpos.x + screen.get_width() + size.x/2

    if playerpos.y > screen.get_height() + (size.x/2): playerpos.y = playerpos.y - screen.get_height() - size.x/2
    if playerpos.y <  -(size.x/2): playerpos.y = playerpos.y + screen.get_height() + size.x/2

    pg.draw.rect(screen, "white", (playerpos,size))


    pg.display.flip()
    clock.tick(60)
