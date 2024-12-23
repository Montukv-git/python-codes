"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

nums = [1,1,2]
#[0,0,1,1,1,1,1,2,2,3,3,4,9,12]

#first solution     O(n)

def remove_dupliactes(nums):
    if not nums:
        return 0

    ans = []
    for num in nums:
        if num not in ans:
            ans.append(num)
    return ans


print(remove_dupliactes(nums))