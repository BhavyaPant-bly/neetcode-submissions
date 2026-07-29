class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
          return False

        dict1={}
        for c in s1:
            if c not in dict1:
                dict1[c]=1
            else:
                dict1[c]+=1
        for i in range(0,len(s2)-len(s1)+1):
            dict2={}
            j=i
            flag=True
            for j in range(i,len(s1)+i):
                if s2[j] not in dict1:
                    flag=False
                    break
                if s2[j] not in dict2:
                    dict2[s2[j]]=1
                else:
                    dict2[s2[j]]+=1
                if dict1[s2[j]] < dict2[s2[j]]:
                    flag=False
                    break
            if flag == True:
               return True
        return False
            
        