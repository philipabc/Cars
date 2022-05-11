# generate random integer values
from random import seed
from random import randint
from random import choice
from random import gauss
from random import random
# seed random number generator
#seed(10)
# prepare a sequence
# sequence = [i for i in range(100)]
# print(sequence)
# # make choices from the sequence
# for _ in range(5):
# 	selection = choice(sequence)
# 	print(selection)

# # generate random numbers between 0-1
# for _ in range(10):
# 	selection = (int)(random()*100%100)
# 	print(selection)

# selection = int(random()*100)
selection = randint(0,100)
#print(selection)
#correct="7"
print("only numbers")
for i in range(0,10):
    print("please input your guess: ",end="" )    
    b=int(input())
    if b!=selection:
        lose=1
        if b>selection:
            print("fail!,please input lower!")
        else:
            print("fail!,please input higher!")
        if i==0:
            print("you have guessed",i+1,"time,you have",10-i-1,"chances left")
        else:
            print("you have guessed",i+1,"times,you have",10-i-1,"chances left")
        if i==9:
            print("you lose!")
    else:
        print("congrats!")
        lose=0
        break
if lose==1:
   print("the correct answer is", selection)
else:
   print("you win!")
   print("the correct answer is", selection)
