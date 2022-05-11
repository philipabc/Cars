import sys
import pygame
def run_game():
    #initialize game and create a dispaly object
    pygame.init()
    screen = pygame.display.set_mode([1200,800])
    pygame.display.set_caption("Alien Invasion")
    # set backgroud color
    bg_color = (230,230,230)

    # game loop
    while True:
        # supervise keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # fill color
        screen.fill(bg_color)
        # visualiaze the window
        pygame.display.flip()
run_game()
# ————————————————
# 版权声明：本文为CSDN博主「OraYang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u010665216/article/details/79086160