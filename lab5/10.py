import re

def spl(st):
    r=r'(?<!^)(?=[A-Z])'
    return re.sub(r,"_",st)
    
s=input()
print(spl(s))