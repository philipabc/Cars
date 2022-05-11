def bounce(num):
    height=100
    for i in range(1,num+1,1):
        height=height/2
    return height    
        
continue_=True
while continue_:
    
    num=int(input("please type the amount of times you want to bounce the ball:"))
    # height=100
    # for i in range(1,num+1,1):
    #     height=height/2
    #     print(f'#{i}: {height=}')
    print(bounce(num))
    
    con=input("do you want do more(e for exit, any key for continue): ")
    if con=="e" or con=="E":
        continue_=False
        print("Exit!")
        
        
        
        
