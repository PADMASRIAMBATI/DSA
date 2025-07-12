# Global scope

def fun1():
    print(x)
def fun2():
    print(x)

x = 3
fun1()
fun2()

# Built-in
from math import e
def fun3():
    print(e)
#e = 3
fun3()