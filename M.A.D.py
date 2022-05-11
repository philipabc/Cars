list1=[]
dev=[]
total2=0
count=0
total=0
hi=int(input("Please type how many number are you going to type in: "))
for i in range(hi):
    hi2=int(input("Please input the numbers one at a time here: "))
    list1.append(hi2)
for k in list1:
    total=total+k
length=len(list1)
answer=total/length
for j in list1:
    devi=answer-j
    dev.append(devi)
length2=len(dev)
# for e in dev:
    # if e<0:
    #     for f in range(0,length2):
    #         if dev[f]==e:
    #             dev[f]=e*-1

for i in range(length):
    if dev[i]<0:
        dev[i]=-dev[i]
    
for a in dev:
    total2=total2+a
FINALANSWER=total2/length2
print(FINALANSWER)