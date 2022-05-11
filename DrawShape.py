#!python
#coding=utf-8
 
import pygame
import sys
import random
 
screen_size = (640, 480)
backgroundcolor = (255, 127, 255)
#pygame初始化
pygame.init()
 
#创建一个窗口
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('Draw rect and circle')
#背景填充
screen.fill(backgroundcolor)

pygame.font.init()
# 4.4 设置字体样式（ps: wryh.ttf是字体库的文件，该文件已经上传，下载后和项目文件放到一个文件夹中）
font = pygame.font.Font("font\wryh.ttf",28)

score=0;
 
while True:
    for event in pygame.event.get():
        #按下关闭按钮，退出程序
        if event.type==pygame.QUIT:
            sys.exit()
        #按下键盘上的任意键，在屏幕上画图
        elif event.type == pygame.KEYDOWN:
            i = random.randint(0, 2)
            drawcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            top = random.randint(0,400)
            left = random.randint(0,500)
            width = random.randint(0,5)
            #画圆
            if i == 0:
                radiu = random.randint(width,100)
                pygame.draw.circle(screen, drawcolor, [top, left], radiu, width)
                score+=1
            #画矩形
            elif i == 1:
                rectwidth = random.randint(0,255)
                rectheight = random.randint(0,100)
                pygame.draw.rect(screen, drawcolor,[left, top, rectwidth, rectheight], width)
                score+=1
            #画椭圆
            else:
                try:
                    rectwidth = random.randint(0,255)
                    rectheight = random.randint(0,100)
                    pygame.draw.ellipse(screen, drawcolor, (left, top, rectwidth, rectheight), width)
                    score+=1
                except ValueError:
                    print('ellipse')
                    pass
    # 4.5 绘制分数

    fontRead = font.render("score:%d"%score,True,(255,0,0))
    screen.blit(fontRead,(100,100))
    #重画屏幕
    pygame.display.update()


# ————————————————
# 版权声明：本文为CSDN博主「蔡金平」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xsc_c/article/details/8973897