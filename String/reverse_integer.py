"""
Input: x = -123
Output: -321

Input: x = 120
Output: 21

"""

def reverse_integer(x):
    rev = int(str(abs(x))[::-1]) * (1 if x > 0 else -1)
    return rev 

x = 123
print(reverse_integer(x))
