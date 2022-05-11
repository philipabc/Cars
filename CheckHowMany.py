count=0 #C
map={}
hi=[2,1,3,6,3,3,4,5,5,6,6,7,8,9,9,10,10]
hi.append(int(input("Please type the number you want to add: ")))
HI=int(input("Please type the number that you want to check in this list: "))
hi[(len(hi)-1)]=100
# print(hi)
# for i in range(len(hi)):
    # if HI==hi[i]:
for i in hi:
    if HI==i:
        
        count+=1
        map={HI:count}
print("The number you typed showed",count,"time(s) in this list")
keys=set(hi)
for k in keys:
    count=0
    for h in hi:
        if k==h:
            count+=1
            map[k]=count
            
#%%
# print(map)
# map[10]=100
# print(map)
# map={a:1001}
# print(map)
# hi=tuple(hi)
# print(hi)

#%%