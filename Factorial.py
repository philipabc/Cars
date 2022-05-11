continue_=True
while continue_:
    
    num=int(input("please type the number you want to be factorialized:"))
    total=1
    for i in range(1,num+1):
        total=total*i
    print(total)
    
    con=input("do you want do more(e for exit, any key for continue): ")
    if con=="e" or con=="E":
        continue_=False
        print("Exit!")


