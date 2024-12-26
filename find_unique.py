"""
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

"""

#my solution

def is_unique(nums):
    unums = set(nums)
    return not len(nums)==len(unums) 

print(is_unique(nums = [1,2,3]))