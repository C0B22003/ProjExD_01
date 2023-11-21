import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#画面のサイズ
    clock  = pg.time.Clock()#時間の設定
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#練習1
    img1 = pg.image.load("ex01/fig/3.png")#練習2番
    img1 = pg.transform.flip(img1,True,False)
    img1s = [img1,pg.transform.rotozoom(img1,6,1.0),pg.transform.rotozoom(img1,10,1.0),pg.transform.rotozoom(img1,4,1.0)]#練習3
    bg_img2 = pg.transform.flip(bg_img,True,False)
    bg_imgs=[bg_img,bg_img2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200
        screen.blit(bg_img, [-x, 0])#練習4
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        

        screen.blit(img1s[tmr%200//50],[300,200])#滑らか
        

        pg.display.update()
        tmr += 1  

        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()

    pg.quit()
    sys.exit()