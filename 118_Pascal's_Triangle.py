'''
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1,numRows):
            layer = [1]
            if i >= 2 :
                nl = result[i-1]
                for j in range(1,len(nl)):
                    s = nl[j-1]+nl[j]
                    layer.append(s)
            layer.append(1)
            result.append(layer)

        return result