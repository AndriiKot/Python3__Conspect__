

Example_1 = 1

if Example_1:
    squares = []
    for i in range(10):
        squares.append(i ** 2)
    print(squares)                     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

if Example_1:
    print([i**2 for i in range(10)])   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


Example_2 = 2

if Example_2:
    print(5 // 2)  # 2
    print(5 / 2)   # 2.5

    print(9 // 2)  # 4
    print(9 / 2)   # 4.5

    print(int(4.5), int(4.4)) # 5 4
    print(float(5), float(3.0))  # 5.0 3.0


Example_3 = 3

if Example_3:
    true, false = True, False
    print(true and false)    # False
    print(true or false)    # True
    print(false or true)    # True
    print((not false) and true)    # True


Example_4 = 4

if Example_4:
    # Boolean
    # Priority
    # not -> and -> or
    print("Priority of boolean operations is noted.")


Example_5 = 5

if Example_5:
    print(bool(None)) # False

    print(bool(0))    # False
    print(bool(0.0))# False
    print(bool(0j)) # False

    print(bool('')) # False
    print(bool([])) # False
    print(bool({}))    # Fasle
    print(bool(())) # False
    print(bool(set()))   # False


Example_6 = 6

if Example_6:
    str1 = 'Yes'
    str2 = "Yes"
    str3 = '''Yes'''
    str4 = """Yes"""
    print(str1, str2, str3, str4) # Yes Yes Yes Yes


Example_7 = 7

if Example_7:
    print('str(5) == \'5\'', str(5) == '5')  # True
    string = '         This is lazyz    \n    '
    print(string.strip())    # 'This is lazy'
    print("DrDre".lower())   # 'drdre'
    print('attention'.upper()) # 'ATTENTION'
    print('smartphone'.startswith('smart'))  # True
    print('smartphone'.endswith('phone'))    # True
    print('another'.find('other'))           # 2
    print('cheat'.replace('ch', 'm'))        # meat
    print(len('Rumpelstiltsjub'))            # 15
    print('ear' in 'earth')                  # True


Example_8 = 8

if Example_8:
    def f(): x = 2
    print(f() == 2)    # False
    print(f() == None) # True
    print(f() is None) # True
    print('' == None)  # False
    print(0 == None)   # False


Example_9 = 9

if Example_9:
    l = [11, 22, 22]
    print(len(l))   # 3


Example_10 = 10

if Example_10:
    y = x = 3
    print(x is y) # True
    print([3] is [3]) # False


Example_11 = 11

if Example_11:
    l = [11, 22, 33]
    l.append(44)
    print(l)          # [11, 22, 33, 44]


Example_12 = 12

if Example_12:
    l = [11, 22, 44]
    l.insert(2, 33)
    print(l)          # [11, 22, 33, 44]


Example_13 = 13

if Example_13:
    l = [11, 22, 33]
    l + [44]
    print(l)       # !!! [11, 22, 33]
    l += [44]
    print(l)       # !!! [11, 22, 33, 44]


Example_14 = 14

if Example_14:
    l = [11, 22, 22, 33]
    l.remove(22)   # !!!
    print(l)       # !!! [11, 22, 33]


Example_15 = 15

if Example_15:
    l = [11, 22, 33, 44]
    l.reverse()
    print(l)       # !!! [44, 33, 22, 11]


Example_16 = 16

if Example_16:
    l = [44, 11, 33, 22]
    l.sort()
    print(l)       # !!! [11, 22, 33, 44]


Example_17 = 17

if Example_17:
    l = [22, 22, 22, 33, 44]
    print(l.index(22))    # 0
    print(l.index(22, 2))  # 2
    print(l.index(22, 1))  # 1
    # print(l.index(22, 3))  ValueError: 22 is not in list


Example_18 = 18

if Example_18:
    stack = [3]
    stack.append(42)
    print(stack)        # [3, 44]
    print(stack.pop())  # !!! 42
    print(stack)        # [3]
    print(stack.pop())  # !!! 3
    print(stack)        # []
    # print([].pop()) IndexError: pop from empty list
