import sys
x=0
while(True):
    x=x+1
    if ((x*2)-7)%3==0:
        print(f'x={x}, y={((x*2)-7)/3}')
        y=((x*2)-7)/3
        if (2*x)-(y*3)==7:
            x2=x*2
            y2=y*3
            print(2*x,"-",3*y,"=7")
            if x==100 or x>100:
                # sys.exit()
                exit()