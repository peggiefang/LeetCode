'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        long = len(nums)
        numss = set(nums)
        numsr = set(range(1,long+1))
        result = list(numsr-numss)
        return result
        
'''
        if nums != []:
            nums.sort()
            for i in range(1,len(nums)+1):
                if i not in nums:
                    nums.append(i)
            del nums[:max(nums)]
        return nums
'''