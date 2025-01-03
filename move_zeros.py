"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def move_zeros(nums):
    for i,num in enumerate(nums):
        if num == 0:
            nums.pop(i)
            nums.append(0)
    return nums
 
print(move_zeros([0,1,0,3,12]))
print(move_zeros([0,1,0,0,0]))
print(move_zeros([0]))
print(move_zeros([]))

