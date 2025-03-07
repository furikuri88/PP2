n=int(input())
def ev(n):
    for i in range(n):
        if i%3==0 and i%4==0: #it can be "i%12"
            yield i
a=ev(n)
print(list(a))