li=input().split()
i=0
k=[0,0,7]
p=0
b=False
while i<len(li):
    if int(li[i])==k[p]:
        p+=1

    if p==3:
        break
    i+=1
if p==3:
    print(True)
else:
    print(False)


