import randomlist
median=randomlist.randomlist(40)
    
def max(num):
    fst=num[0]
    for i in num:
        if fst<i:
            fst=i
    return fst

if __name__ == "__main__":
    fsttmp=max(median)
    print(fsttmp,median)
                
