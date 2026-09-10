class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                x=x+i.lower()
        y=x[::-1]       
        return y==x
        