from randomlist import randomlist
# print(randomlist(10))

mode=[1,2,3,4,4,1,1,1,1,1,3,4,2,4,4,5,5,5,5,5,5,6,0,-1,-1]

# sort the list
length=len(mode)
for b in range(length):
    for k in range(b+1,length):
        if mode[b]>mode[k]:
            tmp=mode[b]
            mode[b]=mode[k]
            mode[k]=tmp
print(mode)

# find the number of occurence for every number
current=0
map={}
count=1
for k in range(1,length):
    if mode[k]==mode[current]:  
        count+=1
    else:
        b=mode[current]
        map[b]=count  
        count=1
        current=k  
    if k==length-1:
        map[mode[k]]=count

print(map)
# get the mode of list---2 steps
valuesList=list(map.values())
print(valuesList)
max=valuesList[0]
# step 1: get the max of the values
for v in valuesList:
    if max<v:
        max=v
# step 2: get the keys of the max values
modes=[]
for (k,v) in map.items():
    if v==max:
        modes.append(k)
print("The mode(s) of your str is",modes)
        


