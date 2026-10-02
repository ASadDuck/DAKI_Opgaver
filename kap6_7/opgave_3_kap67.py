import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
size = pg.Vector2(25,25)
playerpos = pg.Vector2(300,300)
player_speed = 4

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys_pressed = pg.key.get_pressed()

    screen.fill("white")
    if running == False:
        screen.fill("red")

    playerpos.x = ((keys_pressed[pg.K_a] * -player_speed) + (keys_pressed[pg.K_d] * player_speed)) + playerpos.x
    playerpos.y = ((keys_pressed[pg.K_w] * -player_speed) + (keys_pressed[pg.K_s] * player_speed)) + playerpos.y

    pg.draw.rect(screen, "black", (playerpos,size))


    pg.display.flip()
    clock.tick(60)
