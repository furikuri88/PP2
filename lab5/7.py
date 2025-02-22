import re
def stc(st):
    r=r'_'
    rep=""
    sh=re.sub(r,rep,st)
    return sh
s=input("enter snake str: ")
print("camel str:",stc(s))