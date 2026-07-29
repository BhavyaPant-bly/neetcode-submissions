from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return t
        if len(t)> len(s):
            return ""
        length=len(s)+1
        ans=[-1,-1]
        l=0
        seen=0
        count={}
        req = Counter(t)
        for r,key in enumerate(s):
            if seen ==0 and key not in req:
                l=r+1
            elif key not in req:
                continue
            else:
                count[key]=1 if key not in count else count[key]+1
                if count[key]<= req[key]:
                    seen +=1

                elif s[l] == key:
                    while key not in req or count[key] > req[key]:
                        if key in count:
                            count[key]-=1
                        l+=1
                        key=s[l]
                if seen == len(t) and length > r-l+1:
                    length = r-l +1
                    ans=[l,r]
        return "" if ans[0] ==-1 else s[ans[0]:ans[1]+1]