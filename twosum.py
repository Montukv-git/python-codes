"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

nums = [2,7,11,15]
target = 13

#Solution 1      -       Brute force        O(n^2)

def twosum(nums, target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i]+nums[j]  ==  target:
                return [i,j]
            
    return []

#print(twosum(nums, target))

#Solution 2         -   optimal solution with dict with time complexcity of O(n)

def twosumoptimal(nums, target):
    temp_dict   =   {}
    for i,num in enumerate(nums):
        rem =   target  -   num
        if rem in temp_dict:
            return[temp_dict[rem],i]
        
        temp_dict[num]  =   i
    return  []

print(twosumoptimal(nums, target))

