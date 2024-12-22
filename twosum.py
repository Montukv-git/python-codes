"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

#My Solution 1      -       Brute force

def twosum(nums, target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i]+nums[j]  ==  target:
                return [i,j]
            
    return "No Answer"

nums = [2,7,11,15]
target = 13

print(twosum(nums, target))