a, b, c = 11, 22, 33
print(a, b, c) # 11 22 33

print(a, b, c, end=' END STRING\n') # 11 22 33 END STRING
print(a, b, c, sep='', end='\n')    # 112233
print(a, b, c, sep='-')             # 11-22-33

string_1 = 'Long string 1 \nLong string 2'
my_list = string_1.split()    				# ['Long', 'string', '1', 'Long', 'string', '2']
print(string_1, my_list, sep='\n')
print('---'.join(my_list))     				# Long---string---1---Long---string---2

import time

for i in range(5):
    print(f"Message {i}", flush=True)
    time.sleep(1)


import time

for i in range(5):
    print(f"Message {i}")
    time.sleep(1)  # Имитация долгого процесса

from math import *

print(sin(9))


print('asdfsaf' + 'safdsaf')

string


