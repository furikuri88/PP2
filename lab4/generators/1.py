import math
n=int(input())
def squ(n):
    for i in range(n):
        yield i**2
a=squ(n)
print(list(a))