'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

'''

class Solution:
    def intersect(self, nums1, nums2):
        inter=[]
        if len(nums1) > len(nums2):
            
            for i in nums2:
                for j in nums1:
                    if i == j:
                        inter.append(j)
                        nums1.remove(j)
                        break

        else:
            for i in nums1:
                for j in nums2:
                    if i == j:
                        inter.append(j)
                        nums2.remove(j)
                        break

        return inter
            