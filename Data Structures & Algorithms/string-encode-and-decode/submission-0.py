class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            l=len(s)
            res=res+str(l)+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            has=s.find("#",i)
            length=int(s[i:has])
            r=s[has+1:has+1+length]
            result.append(r)
            i=has+1+length
        return result
