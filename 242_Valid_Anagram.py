'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        d = Counter(t)
        if c == d:
            return True
        else:
            return False