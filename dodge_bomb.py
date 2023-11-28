import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    #1爆弾作成
    baku = pg.Surface((20,20))
    pg.draw.circle(baku,(255,0,0), (10,10), 10)
    baku.set_colorkey((0,0,0))
    baku_rect = baku.get_rect() 
    baku_rect.centerx = random.randint(0,WIDTH)
    baku_rect.centery = random.randint(0,HEIGHT)
    #練習2
    vx, vy = +5, +5



    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(baku, baku_rect)
        baku_rect.move_ip(vx, vy)

        pg.display.update()

        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()