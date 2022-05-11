number=float(input("Please enter the first number: "))
op=(input("now please enter your operator: "))
number2=float(input("Please enter the second number: "))
if op=="+":
    print(number+number2)
elif op=="-":
        print(number-number2)
elif op=="*":
            print(number*number2)
elif op=="/":
    print(number/number2)            
# elif op=="**":
    # print(pow(number,number2))
elif op=="**":
    print(number**number2)
else:
    print("invalid operator")
    