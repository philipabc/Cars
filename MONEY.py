howmuchmoneyyouhave=0
again="n"
p=int(input("Please type how much money your going to put in: "))
rate=int(input("Please type the interest rate now:"))
print("ok i will give you one dolloar a month")
time=input("Ok your back how long has it been?(d,w,m,y) ")
time2=int(input("ok how many(how many d's its been etc.)?"))
if time=="d" or time=="w":
    if time=="d":
        if time2>=31:
            m=time2/31
else:
    if time=="m":
        x=p*rate/100.0*time2+p
        rusure=input("you will get this much money are you sure you want to take it out?(y or n)")
        print(x)
        if rusure=="y" or rusure=="Y":
            print("ok now you have",howmuchmoneyyouhave+x,"!")
            agian="n"
        elif rusure=="n" or rusure=="N":
            print("ok check back again bye")
            again="y"
            if again=="y":
                while again=="y":
                    time=input("Ok your back how long has it been?(d,w,m,y) ")
                    time2=int(input("ok how many(how many d's its been etc.)?"))
                    x=p*rate*time2+p
                    rusure=input("you will get this much money are you sure you want to take it out?(y or n)")
                    print(x)
                    if rusure=="y" or rusure=="Y":
                        print("ok now you have",howmuchmoneyyouhave+x,"!")
                        agian="n"
                    elif rusure=="n" or rusure=="N":
                        print("ok check back again bye")
                        again="y"
    elif time=="y":
        x=p*rate/100.0*time2*12+p
        rusure=input("you will get this much money are you sure you want to take it out?(y or n)")
        print(x)
        if rusure=="y" or rusure=="Y":
            print("ok now you have",howmuchmoneyyouhave+x,"!")
            agian="n"
        elif rusure=="n" or rusure=="N":
            print("ok check back again bye")
            again="y"
            if again=="y":
                while again=="y":
                    time=input("Ok your back how long has it been?(d,w,m,y) ")
                    time2=int(input("ok how many(how many d's its been etc.)?"))
                    x=p*rate*time2+p
                    rusure=input("are you sure you want to take it out?(y or n)")
                    print(x)
                    if rusure=="y" or rusure=="Y":
                        print("ok now you have",howmuchmoneyyouhave+x,"!")
                        agian="n"
                    elif rusure=="n" or rusure=="N":
                        print("ok check back again bye")
                        again="y"