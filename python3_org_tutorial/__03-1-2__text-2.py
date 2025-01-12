my_python_str = 'some my string'

print(len(my_python_str)) # 14 build-in fucntion 

print(my_python_str)
print(my_python_str[0])   # 's' 	first character
print(my_python_str[-1])  # 'g' 	last character
print(my_python_str[0:5]) # 'some'  first 5 characters included 0 to 4 index (5 not included, 5 index excluded)
print(my_python_str[3:6]) # 'e m'   characters from index 3 to 5 (6 not included, 6 index excluded)
print(my_python_str[4:])  # ' my string' 		characters from position 4 (included) to the end
print(my_python_str[-4:]) # 'ring'	characters from the forth character from the end to the end

'''
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
'''


'''
    my_ptyhon_str[0:] = 'other string'
    Traceback (most recent call last):
    File "...\__xx__Python3\python3_org_tutorial\__03-1-2__text-2.py", line 19,
    in <module>
        my_ptyhon_str[0:] = 'other string'
'''











