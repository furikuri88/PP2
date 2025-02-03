def f(*k):
    print("uuu: ", k[1])
f("ddd",2,"oppa")

def p(a,b,c):
    print(a)
p(c=2,b=8,a=9)

def mapp(**l):
    print(l["hjjj"])
mapp(a="hlll", hjjj="h")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def cic(gg):
    for x in gg:
        print(x)



