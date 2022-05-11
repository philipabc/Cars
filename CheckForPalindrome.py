cont="y"
while cont=="y" or cont=="Y":
    chr=str(input("Please type the Str you want to Check: "))
    length=len(chr)
    isPalindrome="No"
    if chr=="":
        isPalindrome="yes"
    else:
        for i in range(0,length,1):
            if(chr[i])==(chr[length-1-i]):
                isPalindrome="yes"
                continue
            else:
                isPalindrome="No"
                break
    print("isPalindrome: ",isPalindrome)
    cont=input("Do you want it to repeat?(y or n) ")
