num=int(input("please type the the number rule you want bewteen 1-20:"))
if num==1:
    print("1 is always a factor")
elif num==2:
    print("the factor is 2 if the number is even")
elif num==3:
    print("the facor is 3 if he sum of all digits is divisible by 3")
elif num==4:
    print("the factor is 4 if the last 2 digits of the number is divisible by 4")
elif num==5:
    print("the factor is 5 if the last digit is 0 or 5")
elif num==6:
    print("the factor is 6 if it is divisible by 3 and 2")
elif num==7:
    print("the factor is 7 if all the digits above the ones column minus the last digit times 2 is divisible by 7 if still to big repeat again")
elif num==8:
    print("the factor is 8 if the last 3 digits of the number is divisible by 8")
elif num==9:
    print("the factor is 9 if the sum of the digits is divisible by 9")
elif num==10:
    print("the factor is 10 if teh last digit has a 0 at the end")
elif num==11:
    print("the factor is 11 if the digits above the ones column minus the ones column is divisible by 11 if still to big repeat same process")
elif num==12:
    print("the factor is 12 if it is divisible by 3 and 4")
elif num==13:
    print("the factor is 13 if when you add 4 times the last digit then you delete the last digit and add the 4 imes of the digit you deleted to the rest and that number is divisible by 13")
elif num==14:
    print("the fator is 14 if it is divisible by 2 and 7")
elif num==15:
    print("the factor is 15 if it is divisible by 3 and 5")
elif num==16:
    print("the factor is 16 if the last four digits are divisible by 16 if number too low then take away the last 2 digits then times 4 the rest then add it up if it is divisible by 16 then it is a factor of your number")
elif num==17:
    print("the factor is 17 if when you times 4 the last digit then the rest minus the answer of the ones digit times 4 is divisible by 17")
elif num==18:
    print("the factor is 18 if it is divisibl by 9 and 2")
elif num==19:
    print("the factor is 19 if the numbers above the ones digit plus the ones digit imes 4 is divisible by 19")
elif num==20:
    print("the factor is 20 if it is divisble by 10 and 2")
else:
    print("Out of range please choose 1-20 ERROR")