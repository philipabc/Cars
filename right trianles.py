from colorama import Fore,Back,Style
print("welcome to the auto right triangle maker")
print("please input the height:",end ="")
height=int(input())
print("now please input the width:",end =(" "))
width=int(input())
if height<=1 or width<=1:
    print("plase give a higher number than 2 (restart this)")
else:
    print("thank you!")
    print ("now wait it is processing")   

for i in range(1,height+1):
    for j in range(i):
        print("* ",end="")
    print()
    
print(Fore.RED+"some red text"+Fore.BLUE+" ,some blue text"+Fore.YELLOW+" ,some yelllow text")
print(Back.GREEN+"and with a green background")
print(Style.DIM+"and in dim text",end="")
print(Style.RESET_ALL)
print('back to normal now\n')