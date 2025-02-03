li=input().split()
i=0
b=False
while i+1<len(li):
    if int(li[i])==3 and int(li[i+1])==3:
        b=True
    i+=1
print(b)
