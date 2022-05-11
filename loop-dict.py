# python字典遍历的几种方法
# （1）遍历key值

a={'a': '1', 'b': '2', 'c': '3'}


for key in a:
    print(key+':'+a[key])


for key in a.keys():
    print(key+':'+a[key])

# 在使用上，for key in a和 for key in a.keys():完全等价。

# （2）遍历value值

for value in a.values():
    print(value)

# （3）遍历字典项

for kv in a.items():  # kv 是一个元组，和下面两种写法一个样
    print(kv)


for key,value in a.items():
    print(key+':'+value)


for (key,value) in a.items():
    print(key+':'+value)

