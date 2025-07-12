# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Scope
def fun1():
    a = 1
    print(a)

def fun2():
    b = 2
    print(b)

fun1()
fun2()

def fun3():
    x = 9
    def fun4():
        print(x)
    fun4()
fun3()

