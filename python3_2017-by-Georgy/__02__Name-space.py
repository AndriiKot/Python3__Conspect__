
print(int, float, complex)

some_string = 'some string'

a = b = some_string

print(id(a), id(b), id(some_string))
print(a is b, b is some_string, some_string is a)  # True True True

print(bool, type(True))
print(None)
print(type(None))  # <class 'NoneType'>


def plus(a, b):
	return a + b

print(callable(plus))   # True

copy_fn_plus = plus
print(callable(copy_fn_plus)) # True


print(dir(__builtins__))
vars()   # equivalent locals() or object.__dict__

# !!!
print(dir) # <built-in function dir>
dir = 123
print(dir) # 123
del dir
print(dir) # <built-in function dir>

some_string = 'some string'
print(type(some_string) is str) # True
print(type(some_string) is int) # False

aa, bb, cc = 111, 222, 333
print(aa < bb < cc) # True


print(11 in [33, 22, 11], 22 in (33, 22, 11), 11 in {11: 'aa', 22: 'bb'})  # True True

# !!!
print(False is False in [False]) # True
# or
print((False is False) and (False in [False])) # True
# !!!

print(not 333)  # False
print(not '')   # True
print(not 0)    # True
print(not False) # True
print(not [])    # True
print(not {})    # True
print(not ())    # True

print(not [11, 22, 33])       # False
print(not {'a': 11, 'b': 22}) # False
print(not (11, 22, 33))       # False


some_string = input('Введите строку: ')
print(some_string)
print(len(some_string))

