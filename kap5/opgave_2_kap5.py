import math
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True

main_font = pg.font.Font(None, 30)


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    if running == False:
        screen.fill("red")

    text = main_font.render("i aint doin allat again", True,
                            "black")

    screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height()/2 ))


    pg.display.flip()
    clock.tick(60)


pg.quit()
