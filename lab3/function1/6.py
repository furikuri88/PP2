def sp(x:str):
    words=x.split()
    return words

a=input()
o=sp(a)
i=0
while i<len(o):
    p=len(o)-1-i
    print(o[p],end=" ")
    i+=1
