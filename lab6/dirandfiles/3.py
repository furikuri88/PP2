import os
p="C:/Users/lozis/OneDrive/Desktop/Tor Browser/Browser/plugin-container.exe"
if os.access(p,os.F_OK):
    print(f"path {p} exist\n")
else:
    print(f"path {p} does not exist\n")
print("file: ",os.path.basename(p))
print("dir: ",os.path.basename(os.path.dirname(p)))