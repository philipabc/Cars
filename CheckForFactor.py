x=int(input("Please print the number your using to test:"))
num=int(input("Please type the number you want to be tested:"))
total=num/x
if num%x>0:
    print("This is not divisible by",x)
else: 
    print("This is Divisible by",x)