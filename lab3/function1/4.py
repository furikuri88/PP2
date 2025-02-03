nums=input().split()
def pri(x):
    b=True
    i=2
    while i<x:
        if x%i==0:
            b=False
        i+=1
    if b==True:
        return True
    else:
        return False
    
for y in nums:
    if pri(int(y)) and int(y)!=1 and int(y)!=0:
        print(y)

