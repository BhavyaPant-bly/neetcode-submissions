class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        left =0
        right = len(num)-1
        while left< right:
            if (num[left]+num[right])>target:
                right-=1
            elif(num[left]+num[right]) == target:
                return [left+1,right+1]
            else:
                left+=1
        return [-1,-1]
        