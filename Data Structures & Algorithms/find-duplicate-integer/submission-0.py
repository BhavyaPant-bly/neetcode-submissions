class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique={}

        for num in nums:
            if num in unique:
                return num
            unique[num]=1
        return -1
        