e=input().split()
def uni(e):
    i=0
    while i<len(e):
        j=0
        b=True
        while j<i:
            if e[i]==e[j] and i!=j:
                b=False
            j+=1
        if b==True:
            print(e[i],end=' ')
        i+=1
uni(e)