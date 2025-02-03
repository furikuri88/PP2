#C = (5 / 9) * (F – 32)

def ftc(x):
    global y
    y= (5 / 9)*(x-32)
x=float(input())
ftc(x)
print(y)