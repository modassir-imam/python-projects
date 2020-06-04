import re


def add(x,y):
    print(x+y)
    return x+y

def sub(x,y):
    print(x-y)
    return x-y

def mul(x,y):
    print(x*y)
    return x*y

def div(x,y):
    print(x/y)
    return x/y


print("welcome to calculator")
n = True
x = int(input())
while n:
    print("choose the operation:")
    print("1 : add")
    print("2 : sub")
    print("3 : mul")
    print("4 : div")
    choice = int(input())
    y = int(input())
    if choice == 1:
        x=add(x,y)
    elif choice == 2:
        x=sub(x,y)
    elif choice == 3:
        x=mul(x,y)
    elif choice == 4:
        x=div(x,y)
    else:
        n=False
