"""
Input: x = -123
Output: -321

Input: x = 120
Output: 21

"""

def reverse_integer(x):
    rev = int(str(abs(x))[::-1]) * (1 if x > 0 else -1)
    return rev if -(2**31) <= rev <= (2**31 - 1) else 0

x = 123
print(reverse_integer(x))
