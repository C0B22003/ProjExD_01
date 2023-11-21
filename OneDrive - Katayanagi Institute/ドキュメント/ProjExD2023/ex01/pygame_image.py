import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#画面のサイズ
    clock  = pg.time.Clock()#時間の設定
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1
    img1 = pg.image.load("ex01/fig/3.png")#練習2番
    img1 = pg.transform.flip(img1,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#練習4
        screen.blit(img1,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()