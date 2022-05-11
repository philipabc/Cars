#%%
a=set()
print(f'{a=} {type(a)=}')
a={}
print(f'{a=} {type(a)=}')
a={3,}
print(f'{a=} {type(a)=}')
a.add(5)
print(f'{a=} {type(a)=}')
a.remove(5)
print(f'{a=} {type(a)=}')
a.clear()
print(f'{a=} {type(a)=}')
a.add(5)
print(f'{a=} {type(a)=}')

#%%
a={1,'3','f',"y",100,3.5}
length=len(a)
for _ in range(length):
    a.pop()
    print(a)

#%%
del a
print(f'{a=} {type(a)=}')
