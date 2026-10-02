import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
size = pg.Vector2(25,25)
playerpos = pg.Vector2(300,300)
player_speed = 4
curr_dir = pg.Vector2(0,0)

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys_pressed = pg.key.get_pressed()

    screen.fill("white")
    if running == False:
        screen.fill("red")
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

    playerpos.x = (curr_dir.x * player_speed) + playerpos.x
    playerpos.y = (curr_dir.y * player_speed) + playerpos.y
    pg.draw.rect(screen, "black", (playerpos,size))


    pg.display.flip()
    clock.tick(60)
