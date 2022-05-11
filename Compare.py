def compare(a,b):
    if a<b:
        a1stBox=a
        a2ndBox=b
    else:
        a1stBox=b
        a2ndBox=a
    # print(f'{a1stBox=},{a2ndBox=}')

if __name__ == "__main__":
    compare(int(input("Please type the number you want to compare: ")),int(input("Please type the second number you want to compare: ")))