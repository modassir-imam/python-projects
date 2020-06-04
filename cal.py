import re

print("out magical calculator")
print("type quit to exit the calculator")

pre = 0
run = True

def fun():
    global run
    global pre
    eq = input("ente the equation: ")
    if eq == "quit":
        run = False
    else:
        pre = eval(eq)
        print("you typed ",pre)

while run:
    fun()