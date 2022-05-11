import time
print(
    '''I will give you 100% rate annual but you decide to come 
everyday to get your money and take the money
and put it back in i will you how much you are going to get''')
n=int(input("withdraw and deposit of times:"))
m=5000
n=m*n
r=100/100    #annual interest rate
r=r/n     #interest rate for every period
p=1
t=1
x=0
money=1
import time
print(f'{(start:=time.time())=}')
print(time.ctime())
while True:
    x+=1
    p=money
    money=p*(1+r*t)
    if x%m==0:
        print("day",x,money,time.ctime())
    if x==n:
        break
# print(money)    
print(f'{(stop:=time.time())=}')  
print(f'{((stop-start)//60)=} minutes')
print(f'day={x}, {money=}')
    
# day1:
# p=money=1
# money=r*p*t+p=p(1+rt)

# day2:
# p=money
# money=p(1+rt)   

# day3:
# p=money
# money=p(1+rt)

# day4:
# p=money
# money=p(1+rt)

# day5:
# money=p(1+rt)^5   # here P is the initial principal, it is not the recursive principal


def money(p=1,r=1,t=1):
    return p*(1+r*t)

def compound(times,p=1,annualRate=1,Period=1):
    if times==1:
        return money(p,annualRate,Period)
    else:
        r=annualRate/times
        p=money(p,annualRate,Period)






















































