"""
Input: nums = [3, 0, 1]
Output: 2
Explanation: The range is 
[
0
,
3
]
[0,3], and 2 is missing.

"""

def find_missing_number(nums):
    missing_num = 0
    range_xor = 0
    element_xor = 0

    for i in range(0,len(nums)+1):
        range_xor ^= i

    for j in nums:
        element_xor ^= j

    missing_num =   range_xor ^ element_xor
    return missing_num

nums = [3, 0, 1]
print(find_missing_number(nums))  