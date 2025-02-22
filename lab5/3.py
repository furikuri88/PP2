import re

def fise(st):
    g=  r'^[a-z](?:_[a-z])+$'
    if re.fullmatch(g,st):
        return True
    else:
        return False
stu=["af_bj","a_b_c","a_d","d_q","a_b_c_d"]
se="af_bj a_b_c a_d d_q a_b_c_d add ab g_p_l_o"
for x in stu:
    if fise(x):
        print(x)
sec=se.split()
print("\n","for 2nd:")
for x in sec:
    if fise(x):
        print(x)