

Example_1 = 1

if Example_1:
	squares = []
	for i in range(10):
		squares.append(i ** 2)
	print(squares)

if Example_1:
	print([i**2 for i in range(10)])


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
	print(true and false)	# False
	print(true or false)	# True
	print(false or true)	# True
	print((not false) and true)	# True


Example_4 = 4

if Example_4:
	# Boolean
	# Priority
	# not -> and -> or
	print("Priority of boolean operations is noted.")


Example_5 = 5

if Example_5:
	print(bool(None)) # False

	print(bool(0))	# False
	print(bool(0.0))# False
	print(bool(0j)) # False

	print(bool('')) # False
	print(bool([])) # False
	print(bool({}))	# Fasle
	print(bool(())) # False
	print(bool(set()))   # False


Example_6 = 6

if Example_6:
	str1 = 'Yes'
	str2 = "Yes"
	str3 = '''Yes'''
	str4 = """Yes"""
	print(str1, str2, str3, str4) # Yes Yes Yes Yes

























