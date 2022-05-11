import time,calendar
ticks=time.time()
localtime=time.localtime(ticks)
asctime=time.asctime(localtime)
print(localtime.tm_wday)
cal=calendar.month(2020,1)
print(cal)
print(time.tzname,time.timezone)

Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1
 
print(Money)
AddMoney()
print(Money)

str = input("请输入：")
print ("你输入的内容是: ", str)