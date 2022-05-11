import numpy as np
num1 = float (input("Enter first \
Number: "))
op = input("enter operator:")
if op != "^":
    num2 = float (input("Enter second Number: "))
  
  
if op =="+": 
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    a=num1 * num2
    print(f'{num1 * num2=:0.2f}')
    print(a)
elif op == "**":
    print(num1 ** num2)
elif op == "^":
    print(pow(num1, 1.0/2))  
else:
    print("invalid operator")
    
    
    
    
def num_to_string(num):
    numbers = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three"
    }

    return numbers.get(num, None)

if __name__ == "__main__":
    print(num_to_string(2))
    print(num_to_string(5))