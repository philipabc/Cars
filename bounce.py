def bounce(n):
    height=100
    if(n==0):
        height=100
    else:
        height=bounce(n-1)/2
    return height  
    
if __name__=='__main__':
    for i in reversed(range(1)):
        print(bounce(i))

