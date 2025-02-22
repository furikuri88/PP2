import re

def upsplit(st):
    r=r'[A-Z]'
    return re.split(r,st)
s=input()
print(upsplit(s))