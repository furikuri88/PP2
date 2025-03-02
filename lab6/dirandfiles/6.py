import os
import string
for i in range(0,26):
    u=string.ascii_uppercase
    f=open(f"{u[i]}.txt",'w+')
    f.write("")