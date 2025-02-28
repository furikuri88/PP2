import math
import time
n=int(input("num: "))
t=int(input("time: "))
def sqint(num,tim):
    tis=tim/1000
    time.sleep(tis)
    return math.sqrt(num)
print(f"sqrt of {n} in {t} milliseconds is {sqint(n,t)}")
