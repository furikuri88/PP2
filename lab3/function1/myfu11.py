w=input()
def pol(x):
    i=0
    b=True
    while i<len(x):
        if x[i]!=x[len(x)-1-i]:
            b=False 
            break
        i+=1
    return b
if pol(w):
    print(True)
else:
    print(False)