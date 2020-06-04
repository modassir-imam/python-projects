
x = "my name is Modassir imam and i am a btech grad"
def imam(x):
    y = x.split(" ")
    for i in y:
        for j in i:
            print(j)
        print(i)
    print(x)

imam(x)
n=123
m=23
if n==123 and m==23:
    print("you gessed!!!")
elif n==12 and m==1:
    print("you are about there")
else:
    print("wrong guess!!!")
