# unique/repeatable
# changeable
# unsortable

#%%
print("\n------- string ----------\n")
str0 = ''                   # create ---> C
str1 = "Pythann"
str2 = 'Pythan awesome!'
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])      # read ---- R
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])

# str1[1]="w"  # uchangeable ----> U

print(f'{str1=}')
# del str1[1]           #delete --> D  but the string is uchangeable
print(f'{str1=}')


#%%
print("\n------- tuple ----------\n")
str0 = ()
str9 = (1,)
str1 = tuple("Pythann")
str2 = tuple("Pythan awesome!")
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])

# str1[1]="w"  # uchangeable

print(f'{str1=}')
# del str1[1]           #delete --> D  but the string is uchangeable
print(f'{str1=}')


#%%
print("\n------- list ----------\n")
str0 = []
str1 = list("Pythonn")
str2 = list("Python awesome!")
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])
print(str1[4:6])
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])
print(f'{str1=}')
str1[1] = "w"  # can be change(update) --->U
print(f'{str1=}')
del str1[1]    #delete --> D
print(f'{str1=}')


#%%
print("\n------- set ----------\n")
str0 = set()
str00 = {1, 2}
str1 = set("Python!")
str2 = set("Python awesome!")
print(str1)
print(str2)
str1.add(100) # can be change(updat) --->U
print(str1)
str1.remove(100) # can be delete --->D
print(str1)
print()
print(f'{str1 - str2=}')
print(f'{str1 | str2=}')
print(f'{str1 & str2=}')
print(f'{str1 ^ str2=}')

#%%
print("\n------- map/dictionary ----------\n")
str0={}
str1=dict([('apple',2),('pearl', 3),('orange',15)])
str2=dict(apple=2,pearl=3,orange=15)
print(f'{str1=}')
print(f'{str2=}')
str1['apple'] = 9  # can be change -->U
print(f'line 100: {str1["apple"]=}') 
print(f'line 100: {str1['apple']=}') 
# print(f'line 101: {str1.apple=}') # this is wrong!!!!!
# print(f'line 101: {str1."apple"=}') # this is wrong!!!!!
print(f'{str1=}')
del str1['apple']  #delete --> D
print(f'{str1=}')



print("\n------- ASCII and ordinal ----------\n")
print(ord('中'))
print(ord('a'))
print(chr(ord('中')))
print(chr(ord('a')))

# %%
