"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def move_zeros(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums

 
print(move_zeros([0,1,0,3,12]))
print(move_zeros([0,0,1]))
print(move_zeros([0]))
print(move_zeros([]))

