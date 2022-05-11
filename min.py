# num=[]
# for e in range(int(input("Please type how many numbers you are going to type in: "))):
#     num.append(int(input("Please type the number(s) you want to find the min out of: ")))
import randomlist
median=randomlist.randomlist(20)
    
def min(num):
    fst=num[0]
    for i in num:
        if fst>i:
            fst=i
    return fst

if __name__ == "__main__":
    fsttmp=min(median)
    print(fsttmp,median)
    

