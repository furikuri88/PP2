h=input().split()

def his(x):
    i=0
    while i<len(x):
        j=0
        while j<int(x[i]):
            print('*',end='')
            j+=1
        print("\n",end='')
        i+=1
his(h)