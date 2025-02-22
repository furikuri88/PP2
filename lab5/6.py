import re

def sc(st):
    r=r'\s|\.|,'
    rep=':'
    sh=re.sub(r,rep,st)
    return sh
st=input()
print(sc(st))