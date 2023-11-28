import random
import sys
import pygame as pg


WIDTH, HEIGHT = 800, 600
#練習３
delta = {
    pg.K_UP:(0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0)
}
#練習４
def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    因数rct:こうかとんor爆弾Surfaceのrect
    戻り値:横方向はみだし判定結果（画面内:true/画面外:false）
    """
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
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect() 
    kk_rect.centerx = 400
    kk_rect.centery = 300

    clock = pg.time.Clock()
    #練習１爆弾作成
    baku = pg.Surface((20,20))
    pg.draw.circle(baku,(255,0,0), (10,10), 10)
    baku.set_colorkey((0,0,0))
    baku_rect = baku.get_rect() 
    baku_rect.centerx = random.randint(0,WIDTH)
    baku_rect.centery = random.randint(0,HEIGHT)
    #練習２
    vx, vy = +5, +5



    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rect.colliderect(baku_rect):
            print("Game Over")
            return


        #練習３
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, tpl in delta.items():
            if key_lst[k]: #キーが押されたら＋＝が起きる
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        
        #練習４
        screen.blit(bg_img, [0, 0])
        kk_rect.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_mv[0], -sum_mv[1])


        screen.blit(kk_img, kk_rect)
        #screen.blit(kk_img, [900, 400])
        #練習１
        screen.blit(baku, baku_rect)
        #練習２
        baku_rect.move_ip(vx, vy)
        #練習４
        yoko, tate = check_bound(baku_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        baku_rect.move_ip(vx, vy)



        pg.display.update()

        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()