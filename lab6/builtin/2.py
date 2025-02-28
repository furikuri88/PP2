
def UpLow(st):
    g=str(st)
    u=0
    low=0
    for x in g:
        if x==x.upper():
            u+=1
        elif x==x.lower():
            low+=1
    return u,low
s=input()
print(f"upper: {UpLow(s)[0]} \nlower: {UpLow(s)[1]}")