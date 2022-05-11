# https://blog.csdn.net/theonegis/article/details/49404809?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242
a,s,e,y,o,u,n=0,0,0,0,0,0,0
a=s=e=y=o=u=n=0
for s in range(0, 10):
    for e in range(0, 10):
        for o in range(0, 10):
            for y in range(0, 10):
                for n in range(0, 10):
                    for u in range(0, 10):
                        a+=1
                        # print(a," - ",s," ",e," ",y," ",o," ",n," ",u)
                        # if(((s+y)*100+(e+o)*10+e+u)==(s*1000+o*100+o*10+n) and s!=e and s!=y and s!=o and s!=n and s!=u and e!=y and e!=o and e!=n and e!=u and y!=o and y!=n and y!=u and o!=n and o!=u and n!=u):
                        # if(((s+y)*100+(e+o)*10+e+u) == (s*1000+o*100+o*10+n) and s not in (e, o, y, u, n) and e not in (o, y, u, n) and o not in (y, u, n) and o not in (u, n) and n != u):
                        result={s,e,y,o,u,n}
                        if(len(result)==6):
                            if(((s+y)*100+(e+o)*10+e+u) == (s*1000+o*100+o*10+n)):
                                print(result)
                                print("   see=", s, e, e)
                                print("   you=", y, o, u)
                                print("      _______________")
                                print("soon=", s, o, o, n)
                                print()
print(a)

# a=s=e=y=o=u=n=0
# range_=range(0,10)
# for s,e,y,o,u,n in zip(range_,range_,range_,range_,range_,range_):
#     print(s,e,y,o,u,n)


# a,s,e,y,o,u,n=0,0,0,0,0,0,0
# # if(((s+y)*100+(e+o)*10+e+u)==(s*1000+o*100+o*10+n) and s!=e and s!=y and s!=o and s!=n and s!=u and e!=y and e!=o and e!=n and e!=u and y!=o and y!=n and y!=u and o!=n and o!=u and n!=u):
# if(((s+y)*100+(e+o)*10+e+u) == (s*1000+o*100+o*10+n) and s not in (e, o, y, u, n) and e not in (o, y, u, n) and o not in (y, u, n) and o not in (u, n) and n != u):
#     print("see=", s, e, e)
#     print("you=", y, o, u)
#     print("soon=", s, o, o, n)
#     print()

# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")
# print("Nathan eats 1st cookie")


# for i in range(1,11):
#     if (i==1):
#         print("Nathan eats 1 cookie")
#     else:
#         print("Nathan eats ",i, "cookies")


# while((a:=True)):
#     for _ in range(2):
#         print("print")
#     a=False

# a = list(range(1, 100000))
# b = list(range(150000, 50000, -1))

# a_alone = []

# import time
# start = time.time()
# for i in a:
#     if i not in b:
#         a_alone.append(i)
# end = time.time()

# print(end - start)  # 117s

# a_set = set(a)
# b_set = set(b)

# start = time.time()
# # 求差集得到的是在a里但不在b里的数据集合，a独有
# # 如果a，b不是空集合，a-b为空集合，说明a中的数据全部在b中
# a_alone = a_set - b_set

# end = time.time()

# print(end - start)  # 0.003s

# # 求并集
# c_set = a_set | b_set

# # 求交集，结果集如果为空，说明两个集合没有任何数据是相同的
# d_set = a_set & b_set

# https://blog.csdn.net/HYESC/article/details/104792744?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param

# https://blog.csdn.net/chenpe32cp/article/details/81945335?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param


t=31
t,a=2,t+1

print(t,a)

def t1():
    print(1)
    return 1
def t2():
    print(2)
    return 2
def t3():
    print(3)
    return 3
 
a,b,c = t1(),t2(),t3()
print(a,b,c)