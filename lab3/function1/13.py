import random
n=random.randint(1,20)
print("write a number from 1 to 20")
a=int(input())
if a==n:
    print("harosh")
else:
    print("try again")
while a!=n:
    a=int(input())
    if a==n:
        print("good")
    else:
        print("again")
