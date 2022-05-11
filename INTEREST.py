hi3="i"
hi=input("Hello,how much money are you going to put in? ")
print("Okay!")
hi2=input("ok i will give you a interes of 1 dollar,is that okay? ")
if hi2=="no" or hi2=="No":
    hi3=input("Then how much do you want me to give? ")
    print("the interest rate of this is",hi3,"over",hi)
elif hi2=="yes" or hi2=="Yes":
    print("okay,the interest rate of this is 1 over",hi)