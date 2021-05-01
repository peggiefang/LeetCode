'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.


For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"

'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        Alp = []
        for i in range(ord('A'),ord('A')+26):
            Alp.append(chr(i))
            num = list(str(i) for i in range(1,27))
        Excel_dic = dict(zip(num,Alp))
        ans = []
        if columnNumber <= 26 :
            ans.append(str(columnNumber))
            
        while columnNumber > 26:
            if columnNumber%26 == 0:
                ans.insert(0,str(26))
                columnNumber = (columnNumber//26)-1
            else:
                ans.insert(0,str(columnNumber%26))
                columnNumber = (columnNumber//26)
                
            if columnNumber <= 26:
                ans.insert(0,str(columnNumber))
        result = str()
        for i in ans:
            a = Excel_dic[i]
            result+=a
        return result
