'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true


'''

class Solution:
    def containsDuplicate(self, nums):
        a = set(nums)
        if len(a) != len(nums):
            return True
        else:
            return False