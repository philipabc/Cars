"""
小弹球
1. 搭建项目
2. 绘制一个小球上下移动
3. 弹球
4. 小球碰撞边一次  修改小球颜色值
5. 5个小球同时运行碰撞
6. 计算小球碰撞得分 score +1 显示出来
7. 根据score调整速度 100 200 300
"""
import pygame,sys
import random
 
R = 0
G = 0
B = 0
xx = []
yy = []
ff = []
score = 0
speed = 0
 
"""
一、主函数
"""
def menu():
    # 1.设置窗口标题
    pygame.display.set_caption("小弹球游戏")
    # 2.死循环
    while True:
        # 3.设置背景颜色填充
        screen.fill((255,255,255))
        # 4.调用业务处理函数
        action()
        # 5.调用图形图案绘制函数
        paint()
        # 6.屏幕刷新延迟
        pygame.time.delay(speed)
        # 7.设置窗口刷新屏幕
        pygame.display.update()
 
"""
二、变量声明初始化区域
"""
# 设置窗体
screen = pygame.display.set_mode((800,600),0,0)
 
"""
三、业务逻辑处理区域
"""
def action():
    # 3.1 循环迭代事件监听
    for event in pygame.event.get():
        # 3.2 判断是否退出系统
        if event.type == pygame.QUIT:
            sys.exit()
    # 3.3 执行业务逻辑代码
    global xx,yy,ff,score
    for i in range(0,5):
        # 3.3.1根据飞行方向修改坐标
        if ff[i] == 0:
            xx[i] += 1
            yy[i] += 1
        elif ff[i] == 1:
            xx[i] += 1
            yy[i] -= 1
        elif ff[i] == 2:
            xx[i] -= 1
            yy[i] -= 1
        elif ff[i] == 3:
            xx[i] -= 1
            yy[i] += 1
        # 3.3.2根据坐标值修改飞行方向
        # 下边界
        if yy[i] > 600-30:
            updateBallColor()
            score += 1
            if ff[i] == 0:
                ff[i] = 1
            else:
                ff[i] = 2
        elif xx[i] > 800-30:
            updateBallColor()
            score += 1
            if ff[i] == 1:
                ff[i] = 2
            else:
                ff[i] = 3
        elif yy[i] < 30:
            updateBallColor()
            score += 1
            if ff[i] == 2:
                ff[i] = 3
            else:
                ff[i] = 0
        elif xx[i] < 30:
            updateBallColor()
            score += 1
            if ff[i] == 3:
                ff[i] = 0
            else:
                ff[i] = 1
    # 4.4 根据分数修改速度
    global speed
    if score > 500:
        speed = 1
    elif score > 300:
        speed = 5
    elif score > 100:
        speed = 8
    else:
        speed = 10
"""
四：图形图案绘制区域
"""
def paint():
    # 4.1 绘制小球
    for i in range(0,5):
        pygame.draw.circle(screen,(R,G,B),(xx[i],yy[i]),30,0)
    # 4.2 绘制分数
    # 4.3 初始化字体
    pygame.font.init()
    # 4.4 设置字体样式（ps: wryh.ttf是字体库的文件，该文件已经上传，下载后和项目文件放到一个文件夹中）
    font = pygame.font.Font("font\wryh.ttf",28)
    # 4.5 绘制分数
    fontRead = font.render("score:%d"%score,True,(255,0,0))
    screen.blit(fontRead,(100,100))
"""
五、更改小球颜色
"""
def updateBallColor():
    global R,G,B
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
 
"""
六、初始化函数
"""
def init():
    for i in range(0,5):
        xx.append(random.randint(0,800-30))
        yy.append(random.randint(0,600-30))
        ff.append(random.randint(0,3))
 
if __name__ == '__main__':
    init()
    menu()
 
 
 