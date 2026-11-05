class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        
        def allsubsets(included, index):
            # Base case: if we've made a decision for every number
            if index == len(nums):
                ans.append(included)
                return
            allsubsets(included, index + 1)
            
            allsubsets(included + [nums[index]], index + 1)

        allsubsets([], 0)
        return ans