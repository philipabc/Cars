chse=input("Please type Which form yo want our answer to be in(Fractions or Decimals): ")
num=int(input("Please type the first number to the first fraction: "))
num2=int(input("Please type the second number to the first fraction: "))
num3=int(input("Please type the first number to the second fraction: "))
num4=int(input("Please type the second number to the second fraction: "))
if chse=="d" or chse=="D":
    total=num/num2+num3/num4
    print(total)
elif chse=="f" or chse=="F":
    num5=num2*num4
    num6=num*num4
    num7=num3*num2
    total2=num6+num7
    print(total2,"over",num5)
    for i in range(total2,2,-1):
        if total2%i==0 and num5%i==0:
            total2=total2/i
            num5=num5/i
            print("common factor: ",i,total2,"over",num5)
            # print(f"common factor: {i}: {total2} over {num5}")