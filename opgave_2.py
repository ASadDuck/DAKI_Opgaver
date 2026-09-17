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

    for cube in range(10):
        pg.draw.rect(screen, "black", (25+(cube*50),25, 25,25 ))


    pg.display.flip()
    clock.tick(60)


pg.quit()

