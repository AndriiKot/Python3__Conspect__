import math

def custom_round(n):
    return math.floor(n + 0.5)

print(custom_round(2.5))  #  3
print(custom_round(2.4))  #  2
print(custom_round(2.6))  #  3

