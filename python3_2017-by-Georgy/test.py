a, b = eval(input())
while a != 0 or b != 0:
	print(a, b)
	if a == b:
		print("Было")
		break
	a, b = eval(input())
else:
	print("Не было")
