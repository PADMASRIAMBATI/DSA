from array import *

valus = array('i',[9 , 2, 4, 7, 99])
print(valus)
print(valus.buffer_info())

for i in range(5):
    print(valus[i])