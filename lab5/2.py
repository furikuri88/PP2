import re

def abbb(str):
    reg=r'^ab{2,3}$'
    if re.fullmatch(reg,str):
        return True
    else:
        return False
h=input()
if abbb(h):
    print(True)
else:
    print(False)