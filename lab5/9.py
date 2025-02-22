import re

def spl(st):
    r=r'(?<!^)(?=[A-Z])'
    return re.sub(r," ",st)
    
s=input()
print(spl(s))