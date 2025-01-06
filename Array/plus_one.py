"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

def plus_one(digits):
    if digits:

        nums = int(''.join(map(str,digits)))
        nums+=1
        return list(map(int, str(nums)))
    return digits


print(plus_one([1,2,4]))
print(plus_one([9,9]))