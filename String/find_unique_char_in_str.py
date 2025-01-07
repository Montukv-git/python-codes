"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""

def find_unique_char_in_str(s):
    char_counter = {}
    for c in s:
        char_counter[c] =   char_counter.get(c,0)+1

    for i,c in enumerate(s):
        if char_counter[c]  ==  1:
            return i
        
    return  -1
    

test = ["leetcode",
        "loveleetcode",
        "aabb",
        "x"]

for s in test:
    print(find_unique_char_in_str(s))