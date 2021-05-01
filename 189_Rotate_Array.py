'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 10 and len(nums) > k:
            k = k % len(nums)
            a = nums[len(nums)-k:]
            i = len(nums)-1
            while i >= k:
                nums[i] = nums[i-k]
                i -= 1 
            nums[:k] = a 

        else:
            k = k % len(nums)
            for j in range(k):
                i = len(nums)
                nums.insert(0,nums[-1])
                while  i > 0:
                    nums[i] = nums[i-1]
                    i -= 1
                nums.pop(0)
                j += 1
