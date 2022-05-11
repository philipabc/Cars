import random
def randomlist(num):
    temp=list(range(1000+num))
    list_=random.sample(temp,num)
    return list_

if __name__ == "__main__":
    print(randomlist(10))

# print(randomlist(10))