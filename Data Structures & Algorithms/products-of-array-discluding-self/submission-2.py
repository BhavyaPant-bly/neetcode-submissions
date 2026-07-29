class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero_count=0
        for num in nums:
            if num !=0:
                product = product*num
            if num ==0:
                zero_count+=1

        if zero_count > 1:
            return [0]*len(nums)
        res=[]
        
        for num in nums:
            if num !=0 and zero_count > 0:
                res.append(0)
            else:
                if num !=0:
                    res.append(product//num)
                else:
                    res.append(product)
        return res