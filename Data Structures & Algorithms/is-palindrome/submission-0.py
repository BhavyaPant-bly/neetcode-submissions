class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(c.lower() for c in s if c.isalnum())
        n=len(s)
        # print(s)
        for i in range(0,n//2):
            if(s[i]!=s[n-i-1]):
                return False
        return True