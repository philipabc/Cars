# https://blog.csdn.net/maoersong/article/details/21838303

dict1 = {"z": 1, "b" : "blue", "c" : "color", "g" : "gray", "r" : "red"}
print(dict1["b"])
b="b"
print(dict1[b])
print(f'{dict1["z"]=}')

for(k,v) in dict1.items():  #items()用法
    v=000
    print("dict1[%s] =" % k, v)

# for (k,v) in dict1.iteritems(): #iteritems()用法 
#     print("dict1[%s] =" % k, v)
    
# As you are in python3 , use dict.items() instead of dict.iteritems()

# iteritems() was removed in python3, so you can't use this method anymore.

# Take a look at Python 3.0 Wiki Built-in Changes section, where it is stated:    
# Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().

# Instead: use dict.items(), dict.keys(), and dict.values() respectively.

a={}
b=set()
print(f'{type(a)=}, {type(b)=}')

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
thisset.update([1,3,5,8,9])
thisset.add(2)
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)
thisset = ["Google", "Runoob", "Taobao",[1,4],[5,6],{1,2,3},{'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}]
print(thisset)
thisset = set('abracadabra')
print(thisset)