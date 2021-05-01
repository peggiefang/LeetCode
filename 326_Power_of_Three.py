'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true

'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<= 0:
            return False
        else:
            while n>1:
                if n%3 >=1:
                    return False
                n = n//3
            return True