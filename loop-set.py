a=["q","w","e","r"]
for i in a:
    print(i)

c=enumerate(a)
for i in c:  #i是enumerate的一个元素,是一个元组，类似(i，item)
    print(i)

print()
#这里加了个参数2，代表的是start的值
c=enumerate(a,2)
for i in c:
    print(i)

print()    
#创建一个空字典
b=dict()
#这里i表示的是索引，item表示的是它的值
for i,item in enumerate(a):  #元组(i，item)是enumerate的一个元素
    b[i]=item
print(b)  


# https://blog.csdn.net/cadi2011/article/details/85787932#:~:text=63-,%E9%81%8D%E5%8E%86set%20%E7%94%B1%E4%BA%8Eset%20%E4%B9%9F%E6%98%AF%E4%B8%80%E4%B8%AA%E9%9B%86%E5%90%88%EF%BC%8C%E6%89%80%E4%BB%A5%EF%BC%8C%E9%81%8D%E5%8E%86set,for%20%E5%BE%AA%E7%8E%AF%E5%8F%AF%E4%BB%A5%E9%81%8D%E5%8E%86set&text=%E5%8F%AF%E5%8F%98%E9%9B%86%E5%90%88set%E9%9B%86%E5%90%88,%E9%9B%86%E5%90%88%EF%BC%88frozenset%EF%BC%89%E4%B8%A4%E7%A7%8D%E3%80%82  
print()    
a=set(["q","w","e","r"])
for i in a:
    print(i)

c=enumerate(a)
for i in c:  #i是enumerate的一个元素,是一个元组，类似(i，item)
    print(i)

print()
#这里加了个参数2，代表的是start的值
c=enumerate(a,2)
for i in c:
    print(i)

print()    
#创建一个空字典
b=dict()
#这里i表示的是索引，item表示的是它的值
for i,item in enumerate(a):  #元组(i，item)是enumerate的一个元素
    b[i]=item
print(b)  

# 内置函数iter（），返回一个迭代器对象
print()
for every in iter(a):
    print(every)