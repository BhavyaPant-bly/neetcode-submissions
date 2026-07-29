class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s=[0]*26
        count_t=[0]*26

        for j in range(0, len(s)):
            count_s[ord(s[j])-ord('a')]+=1
            count_t[ord(t[j])-ord('a')]+=1
        for i in range (0,26):
            if count_s[i] != count_t[i]:
                return False
        return True 
        