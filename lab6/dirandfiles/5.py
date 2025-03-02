t=open("tu.txt",'w')
l=['basket','volley','foot','14']
for x in l:
    t.write(f"{x}\n")
t.close()