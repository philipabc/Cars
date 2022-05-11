# """Python实现for无限循环.py"""
 
# __author__ = "李兴球"
# __date__ = 2019/1/3
# __company__ = "风火轮少儿编程"

# """
#    本程序会实例化一个小精灵.它会拷贝自己的一个副本,和海龟画图一样
#    我们把这叫盖图章.接着让图章定位,移动,并且通过相关命令返回图章的坐标,
#    最后让图章不断地旋转.
# """
 
# from sprites import *         # 从精灵模块导入所有命令
 
# bug = Sprite()                # 新建精灵,默认为虫子
# s = bug.stamp()               # 精灵盖图章,返回编号为s
 
# bug.fd(200)                   # 虫子前进200
# bug.stampgoto(s,100,100)      # 虫子编号为s的图章坐标定位到100,100
# bug.stampmove(s,-100,-100)    # 虫子编号为s的图章移动-100,-100
# bug.stampcors(s)              # 返回虫子编号为s的图章的坐标
 
# while 1:bug.right(1) 
 
# class Infinit:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return None
 
# for i in Infinit():
#     print("好嗨哟,你是不是学会了Python的无限循环!")
    
# print("我是永远不会执行到的")

# """
#    美女与图章虚像效果.py
# """
 
# from sprites import *      # 从精灵模块导入所有命令
 
# width,height = 531,800
# screen = Screen()          # 新建屏幕
# screen.setup(width,height) # 设宽度高
# screen.bgpic('姑娘和背景x.png') # 设定背景
# screen.title('美女与图章虚像效果by李兴球')
 
# # 新建角色
# g = Sprite(shape='girl.png',pos=(-22,-26))
# g.setalpha(128)             # 设为半透明
# s1 = g.stamp()              # 盖虚像图章
# s2 = g.stamp()              # 盖虚像图章
 
# clock = Clock()             # 实例化时钟对象
# for x in range(50000):        # 迭代x伍百次
#    g.movestamp(s1,-1,1)     # s1图章向左上角移动
#    g.movestamp(s2,1,1)      # s2图章向右上角移动
#    screen.update()          # 屏幕显示更新
#    clock.tick(30)           # 固定fps为30
  
# dummy = Sprite(visible=False,pos=(52,316))
# dummy.saybordercolor('cyan')
# dummy.saycolor('yellow')
# dummy.say("Hi，雅典娜，你好吗？",100,wait=False)
 
 

"""
   本程序会实例化一只小猫,它会不断地在窗口中走来走去.
"""
 
from sprites import *         # 从精灵模块导入所有命令
 
frames = 'res/cat1.png','res/cat2.png'
cat = Sprite(frames)          # 新建精灵,造型帧序列为frames 
cat.rotatemode(1)             # 设置旋转模式为左右翻转
 
while True:
    cat.fd(10)                # 小猫前进10个单位
    cat.nextcostume()         # 小猫切换到下一个造型
    cat.bounce_on_edge()      # 小猫碰到边缘就反弹
    cat.wait(0.2)             # 小猫等待0.2秒