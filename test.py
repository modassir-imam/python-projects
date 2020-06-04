import datetime as dt
todat = dt.date.today()
print(todat)
time_now = dt.datetime.now()
print(time_now)
print(f"{time_now:%A, %d, %B, %Y ; %H: %M: %S: %f}")
print(f"{time_now:%c}")
d = dt.date(2017,11,21)
e = dt.date(2015,9,11)
diff = d - e
print(diff)
#x = input("enter the value of x:")
#print(x)
print(d.year)
print(d.month)
print(d.day)
n=100
if n==10:
    print("its all good here")
else:
    print("try again")
x = input()
x = int(x)
if x<10:
    print("no is less than 10")
    print("you are a dog")
    i=x*10
    print(i)
elif x>=10 and x<20:
    print("no lies between 10 and 20")
else:
    print("no is greater than 20")
print("end if if else ladder")

imam = "khan"
x=1
for x in range(10):
    print(x)
print("all done")