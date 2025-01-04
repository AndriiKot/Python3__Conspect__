print('string 1' + ' plus ' + 'string 2')
print('srt*' * 3)
print(3 * '*str')
print(1.2 + 5)
print(1.1 + 2.2)

big_string = 'big string 1 next big string 2'
print(big_string.split())
print(dir())    # выводит содержимое пространство имён 
print(
	'string 1 ' * 3,
	3 * 'string 1',
	'STRING' + ' other string',
	100 + 0.2,
sep='\n'
)

import math
print(math.sin(9))

from math import *
print(sin(9))

var1, var2, var3 = 11, 22, 33
print(var1, var2, var3)

var1 = var2 = var3 = 101
del(math)
print(var1, var2, var3)


print(dir())
del(var1)
print(dir())

for ind in dir():
    if not ind.startswith('__'):
        del locals()[ind]

print(dir())

import sys

a = b = c = 100500

print(sys.getrefcount(a))

print(id(a), id(b), id(c))

chr1, chr2, chr3, *chrs = 'some strings'
print(chr1, chr2, chr3, chrs)	

chr1, chr2, chr3, *chrs = 'abc'
print(chr1, chr2, chr3, chrs)

a = 1
b = 1
c = 1
print(id(a), id(b), id(c))
print(a is b, b is c, c is a)    # True True True

	

