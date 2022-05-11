a = 500

def function1(a):
  print("函数中局部变量a的地址：", id(a))
  a = 100  # 更改之后
  print("指向100后的局部a 和 100的地址：", id(a), id(100))

print("全局a和500的地址：", id(a), id(500))
function1(a)
print("函数调用完之后全局a的地址：", id(a))
# ————————————————
# 版权声明：本文为CSDN博主「地质学家dm」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_38727847/article/details/103222616