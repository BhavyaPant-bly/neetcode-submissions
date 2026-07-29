class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        max_length=0

        unique_arr=[]

        for num in unique:
            unique_arr.append(num)
        unique_arr=sorted(unique_arr)
        prev=-1
        for i,num in enumerate(unique_arr):
            if i == 0:
                prev = num
            if num == prev+1:
                length+=1
            else:
                length=1
            prev=num
            max_length=max(max_length,length)
        return max_length






        