import re

def ul(st):
    r=r'^[A-Z][a-z]+$'
    if re.fullmatch(r,st):
        return True
    else:
        return False
st="Ann bjn Jllkkkk OOO pLo UwU Ibn"
sts=st.split()
for x in sts:
    if ul(x):
        print(x)