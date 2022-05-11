x = 2
print("2 ", id(2))
print("x=2 ", id(x))
L = [1, 2, 3]
M = L
print('L ', id(L))
print('M=L ', id(M))
print('L[0]=1 ', id(L[0]))
L[0] = 2
print('L ', id(L))
print('L[0]=2 ', id(L[0]))
print('L[1]=2 ', id(L[1]))

aa = 1999839
bb = 1999839
print(id(aa), id(bb), id(1999839))
print('aa == bb:', aa == bb)
print('aa is bb:', aa is bb)

a = 0
print(id(a))
a = 2
print(id(a))
a = 3
print(id(a))
a = 4
print(id(a))


def process(a):
    a(1, 2, 3)


class A:
    def run(self, a, b, c):
        print(a, b, c)


val = A()
process(val.run)


def change(val):
    print('val ', id(val))
    print(val)
    val.append(100)
    print('val ', id(val))
    print(val)
    val.append(['T', 'Z', 'Y'])
    print('val ', id(val))
    print(val)
    val = ['T', 'Z', 'Y']
    print('val ', id(val))
    print(val)
    val = ['T']
    print('val ', id(val))
    print(val)
    val = 5
    print(val)
nums = [0]
print('nums ', id(nums))
change(nums)
print('nums ', id(nums))
print(nums) 
    
def change(val):
    print(val)
    val = 0
    print(val)
num = 1
change(num)
print(num) #输出结果为1   

c = {'name':'xufive', 'age':51}
print(c)
{'name': 'xufive', 'age': 51}
print(*c)
print('name:{name}, age:{age}'.format(**c))
    