import random
import sys
import pygame as pg


WIDTH, HEIGHT = 800, 600
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}
def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    original_kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 1.0)
    kk_rect = kk_img.get_rect()
    kk_rect.centerx = 400
    kk_rect.centery = 300
    baku = pg.Surface((20, 20))
    pg.draw.circle(baku, (255, 0, 0), (10, 10), 10)
    baku.set_colorkey((0, 0, 0))
    baku_rect = baku.get_rect()
    baku_rect.centerx = random.randint(0, WIDTH)
    baku_rect.centery = random.randint(0, HEIGHT)
    vx, vy = +5, +5
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        if kk_rect.colliderect(baku_rect):
            print("Game Over")
            return
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        if sum_mv[0] > 0:  # 右キーが押されたとき
            kk_img = pg.transform.flip(original_kk_img, True, False)
        elif sum_mv[0] < 0:  # 左キーが押されたとき
            kk_img = original_kk_img
        if sum_mv[1] > 0:  # 下キーが押されたとき
            kk_img = pg.transform.rotate(original_kk_img, 90)
        elif sum_mv[1] < 0:  # 上キーが押されたとき
            kk_img = original_kk_img
        elif tuple(sum_mv) == (+5 , -5):  
            kk_img = pg.transform.rotozoom(kk_img, 45, 1.0)
        elif tuple(sum_mv) == (-5 , -5):  
            kk_img = pg.transform.rotozoom(kk_img, 135, 1.0)
        elif tuple(sum_mv) == (+5 , +5):  
            kk_img = pg.transform.rotozoom(kk_img, -45, 1.0)
        elif tuple(sum_mv) == (-5 , +5):  
            kk_img = pg.transform.rotozoom(kk_img, -135, 1.0)
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rect)
        screen.blit(baku, baku_rect)
        baku_rect.move_ip(vx, vy)
        yoko, tate = check_bound(baku_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        baku_rect.move_ip(vx, vy)
        pg.display.update()
        tmr += 1
        clock.tick(30)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
