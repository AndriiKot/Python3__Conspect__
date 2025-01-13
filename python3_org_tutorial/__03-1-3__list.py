# 1
squares = [4, 9, 16, 25]

print(squares)     # [4, 9, 16, 25]
print(squares[0])  # 4
print(squares[-1]) # 25
print(squares[1:2]) # [9]
print(squares[1:3]) # [9, 16]
print(squares[-3:]) # [9, 16, 25]


# 2
cubes = [8, 27, 65, 125]

cubes[2] = 64
print(cubes) # [8, 27, 64, 125]

cubes.append(216)
print(cubes) # [8, 27, 64, 125, 216]

cubes.append(7 ** 3)
print(cubes) # [8, 27, 64, 125, 216, 343]


# 3
rgb = ["Red", "Green", "Blue"]
rgba = rgb

print(id(rgba) == id(rgb)) # True

rgba.append("Alph")
print(rgb)

correct_rgba = rgba[:]
print(correct_rgba)     # ["Red", "Green", "Blue", "Alph"]
print(correct_rgba[-1]) # "Alph"
print(id(correct_rgba) == id(rgba)) # False !!!

# 4
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[2:6])   # ['c', 'd', 'e', 'f']

# replace some value
letters[2:5] = ['C', 'D', 'E']
print(letters)        # ['a', 'b', 'C', 'D', 'E', 'f', 'g']


# remove element 
letters[2:5] = []
print(letters)        # ['a', 'b', 'f', 'g']


# 5 
some_arr = [11, 22, 33, 44, 55]
print(len(some_arr))  # 5












