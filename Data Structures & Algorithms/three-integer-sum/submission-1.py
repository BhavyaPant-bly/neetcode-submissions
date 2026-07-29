class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=set()
        answer=set()

        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                k=-1*(nums[i]+nums[j])
                if k in target:
                    arr=[nums[i],nums[j],k]
                    arr=tuple(sorted(arr))
                    if arr not in answer:
                        answer.add(arr)
            target.add(nums[i])
        ans_arr=[list(item) for item in answer]
        return ans_arr
