import os
p="C:/Users/lozis/OneDrive/Desktop/python/labs/lab6/dirandfiles"
print("existence: ",end="")
if os.access(p,os.F_OK):
    print(True)
else:
    print(False)
print("readability: ",end="")
if os.access(p,os.R_OK):
    print(True)
else:
    print(False)
print("writability: ",end="")
if os.access(p,os.W_OK):
    print(True)
else:
    print(False)
print("executability:",end=" ")
if os.access(p,os.EX_OK):
    print(True)
else:
    print(False)