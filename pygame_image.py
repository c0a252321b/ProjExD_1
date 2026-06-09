import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img,True,False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img,True,False)
    #(surface,左右反転,上下回転)-True or False
    kt_rct = kt_img.get_rect()
    kt_rct.center = 300, 200
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: #keylstの中のK_UP(上矢印)が押されたら
            kt_rct.move_ip((0,-1)) #(0,-1)動かす
        if key_lst[pg.K_DOWN]: 
            kt_rct.move_ip((0,1)) 
        if key_lst[pg.K_LEFT]: 
            kt_rct.move_ip((-1,0)) 
        if key_lst[pg.K_RIGHT]: 
            kt_rct.move_ip((1,0)) 
        else:
            kt_rct.move_ip((-1,0)) #キーが押されていないときに左に動かす

        
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        #screen.blit(kt_img, [300,200]) 300,200の位置に画像を配置
        screen.blit(kt_img, kt_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()