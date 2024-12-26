"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

#solution

def rotate(nums, k):
    n = len(nums)
    k=k%n
    nums[:] = nums[-k:]+nums[:-k] 

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ([10], 100, [10]),
    ([1, 2, 3, 4], 0, [1, 2, 3, 4]),
    ([1, 2, 3, 4], 6, [3, 4, 1, 2]),
    ([1, 1, 1, 2, 2, 3], 2, [2, 3, 1, 1, 1, 2]),
    ([5, 5, 5, 5], 3, [5, 5, 5, 5]),
    ([1, 2, 3], 1, [3, 1, 2])
]

# testing multiple cases
for i, (nums, k, expected) in enumerate(test_cases):
    original = nums[:]
    rotate(nums, k)
    print(f"Test {i + 1}: {'Pass' if nums == expected else 'Fail'} (Input: {original}, k={k}, Output: {nums}, Expected: {expected})")