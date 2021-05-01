'''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

'''

class Solution:
    def reverse(self, x: int) -> int:
        xm = abs(x)
        xm = str(xm)
        xl = [i for i in xm]
        for j in range(len(xl)):
            a = xl.pop()
            xl.insert(j,a)
        result = ''.join(xl)
        result = int(result)
        
        if x > 0 and result < (2**31)-1:
            return result
        elif x < 0  and -result > -(2**31):
            return -result
        else :
            return 0
