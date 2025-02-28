def pal(s):
    if list(s)==list(reversed(s)):
        return True
    else:
        return False
s=input()
print(pal(s))
