'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3

'''



class Solution:
    def repeatedNTimes(self, A):
        N = (len(A))//2
        A.sort()
        if A.count(A[N-1]) == N:
            return A[N-1]
        else: 
            return( A[N])
        