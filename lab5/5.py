import re 

def anb(st):
    r=r'\ba.*b\b'
    if re.fullmatch(r,st):
        return True
    else:
        return False
s=input().split()
for x in s:
    print(f"{x}:{anb(x)}")