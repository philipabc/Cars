cont="y"
while cont=="y" or cont=="Y":
    chr=str(input("Please type the String you want to Check: "))
    if len(chr)==0:
        print(f'Empty string is a Palindrome!')
    elif chr==chr[::-1]:
        print(f'{chr=} is a Palindrome!')
    else:
        print(f'{chr=} is not a Palindrome!')