# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files
#print(help("modules"))
#print(help("math"))

import math as m
#from math import pi
print(f"Pi value is {m.pi}")
print(f"Exponential constant value is {m.e}")

import math
a, b, c, d, e= 1, 2, 3, 4, 5
print(f"a with Exponential constant {math.e * a}")
print(f"b with Exponential constant {math.e * b}")
print(f"c with Exponential constant {math.e * c}")
print(f"d with Exponential constant {math.e * d}")
print(f"e with Exponential constant {math.e * e}")