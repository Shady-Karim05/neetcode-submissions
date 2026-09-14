class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        neg=False
        if n<0:
            neg=True
            n=n*-1
        while(n>0):
            if n%2==1:
                res=res*x
            x=x*x
            n=n//2
        if neg:
            return 1/res
        return res