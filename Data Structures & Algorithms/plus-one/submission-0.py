class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=""
        r=[]
        for i in digits:
            res=res+str(i)
        result=int(res)+1
        for j in str(result):
            r.append(j)
        return r
