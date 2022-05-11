from randomlist import randomlist

# print(randomlist(10))

sample=[1,2,3,4,4,1,1,1,1,1,3,4,2,4,4,5,5,5,5,5,5,6,0,-1,-1]

# find the number of occurence for every number: make a map, use set as the key of the map

def makeMap(mode):
    map=dict()
    keys=set(mode)
    for k in keys:
        count=0
        for h in mode:
            if k==h:
                count+=1
                map[k]=count
    print(map)
    return map

map = makeMap(sample)

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
        


