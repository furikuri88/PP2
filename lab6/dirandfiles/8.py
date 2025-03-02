import os
p="C:/Users/lozis/OneDrive/Desktop/python/labs/lab6/dirandfiles/torem.txt"
if os.access(p, os.F_OK):
    os.remove(p)
    print(f"file \'{os.path.basename(p)}\' in dir \'{os.path.basename(os.path.dirname(p))}\' deleted")
else:
    print("dir or file or both don't exist")