'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


from itertools import combinations

class Solution(object):
    def twoSum(self,nums,target):
      nl = list(combinations(nums,2))
      for i in range(len(nl)):
        ans = sum(nl[i])
        if  ans == target :
          return [nums.index(nl[i][0]),nums.index(nl[i][1],nums.index(nl[i][0])+1)]
