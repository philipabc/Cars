import sys,pygame

pygame.init()
size=width,height=1200,800
speed=[2,2]
black=0,0,0
screen=pygame.display.set_mode(size)
ball=pygame.image.load("images/sphere.png")
ballrect=ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        ballrect=ballrect.move(speed)
        if ballrect.left<0 or ballrect.right>width:
            speed[0]=-speed[0]
        if ballrect.top<0 or ballrect.bottom>height:
            speed[1]=-speed[1]
        screen.fill(black)
        screen.blit(ball,ballrect)
        pygame.display.flip()

# 作者：网络爱好者Lxy
# 链接：https://www.jianshu.com/p/ef432c79a366
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处
