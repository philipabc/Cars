l1=(1,4,5,1,11,7,2,19,6,3,10,4,8)#C
l2=(1,4,7,2,9,6,3,0,4,8,10,7,3,7)
RIGHT=list(l2)
LEFT=list(l1)
BOTH=list(l1)
BOTH.extend(l2)
EXTRA=[]
EXTRA.extend(BOTH)
print("left one:",l1)
print("right one:",l2)
hi=str(input("Please type which you want to find out in this venn diagram(right or left or left and right and no common type both): "))
map={}
count=0
if hi=="right" or hi=="Right":#R
    for i in l1:
        count=0
        for e in l2:
            if i==e:
                count+=1#U
                map[i]=count
    print("Common:",end=" ")
    for i in map:                
        print(i,end=" ")
    print()   
    print("List:",RIGHT)
    for i in map:
        for k in range(len(l2)):
            if l2[k]==i:
                RIGHT.remove(l2[k])#D
            
    print("Answer:",RIGHT)
elif hi=="left" or hi=="Left":
    for i in l1:
        count=0
        for e in l2:
            if i==e:
                count+=1#U
                map[i]=count
    print("Common:",end=" ")
    for i in map:                
        print(i,end=" ")
    print()   
    print("List:",LEFT)
    for i in map:
        for k in range(len(l1)):
            if l1[k]==i:
                LEFT.remove(l1[k])#D
            
    print("Answer:",LEFT)
elif hi=="both" or hi=="Both":
    for i in l1:
        count=0
        for e in l2:
            if i==e:
                count+=1#U
                map[i]=count
    print("Common:",end=" ")
    for i in map:                
        print(i,end=" ")
    print()   
    print("List:",BOTH)
    for i in map:
        for k in range(len(BOTH)):
            if BOTH[k]==i:
                EXTRA.remove(BOTH[k])#D
            
    print("Answer:",EXTRA)
