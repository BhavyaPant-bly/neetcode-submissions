# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         target=set()
#         answer=set()

#         for i in range(0,len(nums)):
#             for j in range(i+1, len(nums)):
#                 k=-1*(nums[i]+nums[j])
#                 if k in target:
#                     arr = tuple(sorted([nums[i], nums[j], k]))
#                     answer.add(arr)
#             target.add(nums[i])
#         ans_arr=[list(item) for item in answer]
#         return ans_arr
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]

        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1

            while left<right:
                three_sum= nums[i]+nums[left]+nums[right]
                if three_sum>0:
                    right-=1
                elif three_sum<0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left < right:
                        left+=1
        return res