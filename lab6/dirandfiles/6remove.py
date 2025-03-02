import os
import string
for i in range(0,26):
    u=string.ascii_uppercase
    os.remove(f"{u[i]}.txt")
    