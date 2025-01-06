"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""

# XOR solution
# XOR operation: duplicates cancel out (a ^ a = 0), and 0 ^ a = a.
# Using ^= to efficiently find the single number with constant space.

def find_single_number(nums):
    x=0
    for i in nums:
        x ^= i
    return x

test_cases = [
    [1],
    [1,1],
    [1,1,2],
    [3,3,4,5,4,5,9,7,7]
]

print(find_single_number(test_cases[3]))