import sys

number=int(input("Please inout the number that will be factorized: "))
next=1
prev=number
for i in range(1,number+1):
    # next=i
    if i==prev:
        sys.exit(0)
    for e in range(1,number+1):
        if i*e==number:
            print(e,"and",i,"is a factor")
            prev=e