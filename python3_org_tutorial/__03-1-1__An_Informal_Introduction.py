# this is the first comment
spam = 1 # and this is the second commnet
         # ... and now a third!

text = "# This is not a comment because it`s inside quotes."

#Numbers
2 + 2       # 4
50 - 5*6    # 20
(50 - 5*6) / 4  # 5.0
8 / 5           # 1.6 division always returns a floating-point number
10 / 5          # 2.0 !!!

int5 = 5
int5            # 5
float(int5)     # 5.0
int5            # 5   !!!

float5 = 4.0    # 4.0
int(float5)     # 4
float5          # 4.0 !!!

17 // 3         # 5
17 % 3          # 2
5 ** 2          # 25

round(3.5)      # 3 !!!
round(2.5)      # 2 !!!


import math

def custom_round(n):
    return math.floor(n + 0.5)

# Примеры
print(custom_round(2.5))  # Вывод: 3
print(custom_round(2.4))  # Вывод: 2
print(custom_round(2.6))  # Вывод: 3



