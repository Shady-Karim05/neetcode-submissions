class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        result=[]
        for i in digits:
            res=res+str(i)
        r=int(res)+1
        for j in str(r):
            result.append(j)
        return result
