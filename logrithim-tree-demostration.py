# return the natural logarithm of x (to base e)

# log(a,(Base)) : This function is used to compute the natural logarithm (Base e) of a. 
# If 2 arguments are passed, it computes the logarithm of desired base of argument a, numerically value of log(a)/log(Base).

# https://www.geeksforgeeks.org/log-functions-python/

import math

root_size=10000
numOfGroups=1    # how many groups/nodes for any layer

a=root_size      # root size  
groupSize=a      # the group size(node size) for any layer
b=6              # base
x=0              # layer/exponent/log
while True:
    a=a/b
    x+=1         
    if a<=6:     # loop end condition: final group size would be not more than 6
        print(x)
        print(f'logarithm of base {b} of {root_size}: {math.log(root_size,b)=}')
        print(f'{a=} {b=} {math.log(a,b)=}')
        break        

# to get how many groups/nodes for any layer
# to determine the group size for any layer