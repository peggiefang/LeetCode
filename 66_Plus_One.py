'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

'''


class Solution:
    def plusOne(self,digits):
        digits[-1] = digits[-1]+1
        i = -1
        while digits[i] >=10:
            if len(digits) > abs(i) :
                digits[i] = 0
                digits[i-1] = digits[i-1]+1
                i -= 1
                print(digits)
                print(i)
            else:
                digits.insert(0,1)
                digits[i] = 0
        return digits