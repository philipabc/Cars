r=int(input('please input the annual interest rate: '))
t=int(input('how many years do you expect to deposit: '))
p=int(input('how much do you want to deposit(principal): '))
print(f"so, you deposit ${p} for {t} year(s) at the annual interest rate of {r}%")
r=r/100
money=p*(1+r*t)
print(f"you can expect to get ${money} back (principal included)")
print('if you change your mind, you can withdraw your money in advance, and get the interest by day, but the annual interest rate will be only half')
print(f'That means the daily rate is {r/2/365=}%')
print('some day later you can come back to our bank to withdraw your money in total of how many days its been')
actualTime=int(input("your back! How many days has it been?: "))
actualTime=actualTime/365
if actualTime<t:
    if actualTime<t-4:
        r=r/4
    elif actualTime<t-5:
        r=r/5
    else:
        r=r/2
money=p*(1+r*actualTime)
print(f"you get ${money} back (principal included. thank you, have a good day!)")