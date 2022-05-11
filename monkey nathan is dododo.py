a = 1534
b = 0
for _ in range (9):
    b=b + 1
    print ("Day",b,a,"Banana")
    a=a / 2 - 1
    
    
last = 1
for b in range (9):
    last=(last +1)*2
    print ("Day",b,last,"Banana")
    