import os
f=os.listdir(path='C:/Users/lozis/OneDrive/Desktop/Tor Browser/Browser')
print("only dir:","\n")
for x in f:
    if os.path.isdir(os.path.join('C:/Users/lozis/OneDrive/Desktop/Tor Browser/Browser',x)):
        print(x)

print("\n","only files:","\n")
for x in f:
    if os.path.isfile(os.path.join('C:/Users/lozis/OneDrive/Desktop/Tor Browser/Browser',x)):
        print(x)
        
print("\n","files and dirs:","\n")
for x in f:
    print(x)