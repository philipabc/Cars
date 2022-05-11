"""
满天星：
绘制100颗小星星：随机产生的
1.小星星移动：  左上角到右下角移动  循环形式
2.随机颜色 闪烁 修改一次
"""
import pygame,sys
# 导入随机函数模块
import random
# 窗体
screen = pygame.display.set_mode((800,600),0,0)
#坐标值
xx = []
yy = []
# 加载图片（如果需要替换成好看的背景图片）
back = pygame.image.load("images/sphere.png")
"""
第六部分：初始化函数
"""
def init():
    # 循环迭代初始化
    for i in range(0,100):
        xx.append(random.randint(0,800))
        yy.append(random.randint(0,800))
        """
第四部分：业务逻辑处理区域
"""
def action():
    # 4.1 循环遍历所有的事件监听
    for event in pygame.event.get():
        # 4.2 判断是否退出系统
        if event.type == pygame.QUIT:
            sys.exit()
    # 星星移动
    for i in range(len(xx)):
        # 1.更改坐标值
        xx[i] += 1
        yy[i] += 1
        # 2.循环
        if xx[i] > 800:
            xx[i] = 0
        if yy[i] > 800:
            yy[i] = 0
            """
第五部分：图形图案绘制
"""
def paint():
    # 5.1 初始化字体
    pygame.font.init()
    # 5.2 设置字体样式（ps: wryh.ttf是字体库的文件，该文件已经上传，下载后和项目文件放到一个文件夹中）
    font = pygame.font.Font("wryh.ttf", 28)
 
    for i in range(len(xx)):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        # 5.3 设置字体内容以及颜色
        fontRead = font.render("*", True, (R, G, B))
        # 5.4 绘制小星星
        screen.blit(fontRead, (xx[i], yy[i]))
 
    # 月亮
    pygame.draw.circle(
        screen,  # 绘制在哪个窗体上
        (255, 255, 255),  # 圆的颜色
        (100, 100),  # 圆的圆心点坐标
        50,  # 圆的半径
        0)  # 圆的线宽 0默认是实心圆  >0 空心圆
    pygame.draw.circle(
        screen,  
        (0, 0, 0),  
        (80, 80),  
        50,  
        0)  
    """
第一部分 主函数(设置窗口信息)
"""
def menu():
    # 1.设置窗口标题
    pygame.display.set_caption("满天星")
    # 2.死循环
    while True:
        # 3.填充背景颜色（R,G,B）
        screen.fill((0,0,0))
        # 绘制哪张图，以及起始点位置
        # screen.blit(back,(0,0))
        # 4.调用业务逻辑模块
        action()
        # 5.调用图形图像绘制
        paint()
        # 控制刷新频率，设置每隔10毫秒刷新一次屏幕
        pygame.time.delay(10)
        # 6.刷新屏幕
        pygame.display.update()
        
if __name__ == '__main__':
    init()
    menu()
 
 