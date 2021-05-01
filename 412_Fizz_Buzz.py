'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = [str(x) for x in range(1,n+1)]
        for i in range(1,n//3+1):
            idx3 = 3*i
            l[idx3-1]= 'Fizz'
        for j in range(1,n//5+1):
            idx5 = 5*j
            l[idx5-1]= 'Buzz'      
        for k in range(1,n//15+1):
            idx15 = 15*k
            l[idx15-1]= 'FizzBuzz'
        return l