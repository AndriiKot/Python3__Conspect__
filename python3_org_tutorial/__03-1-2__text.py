3 * 'some string '           # 'some string some string some string '
'next some string ' * 2      # 'next some string next some string '
3 * 'string' + ' plus '      
                              
'string 1 ' 'string 2'       #   'string 1 string 2'
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)


'spam eggs' # 'spam eggs'
"Paris"     # 'Paris'
'1975'      # 1975
"doesn't"   # "doesn't"
'doesn\'t'  # "doesn`t"
r'C:\some\name' # 'C:\\some\\name'

"""\ 
    Some text 1
  Some text 2
      Some text 3
"""
''' Next text \
  Some next text 1
        Some next text 2
Some next text 3                         
'''

long_string = '''It is \
very strong \
string \
very \
long \
string'''

print(long_string)    # It is very strong string very long string

string1 = 'Some string'
print(string1[0], string1[1])  # S 0
print(string1[0], string1[1], string1[2], sep='')  #Som
print(string1[0], string1[1], string1[2], sep='-', end=' ENDING ')  # S-o-m ENDING
print()


print(string1[-1])  # g
print(string1[-2])  # n
print(string1[-3])  # i

                                                        
print(string1[2:8])  		# me str
print(string1[-5:-2]) 		# tri

print(string1[:5])			# Some
print(string1[0:5])         # Some

print(string1[5:(-1)])      # strin
print(string1[5:])			# string


len('Long String')          # 11

