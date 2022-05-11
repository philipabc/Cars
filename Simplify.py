num=int(input("Please type the first number you want to be Simplified: "))
num2=int(input("Please type the second number you want to be Simplified: "))
for i in range(num+1,1,-1):
    if num%i==0 and num2%i==0:
        num=num/i
        num2=num2/i
        print(f'{i}: {num} over {num2}')