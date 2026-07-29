import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window=[]
        ans=[]
        i=0
        n=len(nums)
        while i<k:
            heapq.heappush(window,(-nums[i],-i))
            i+=1
        i-=1
        while i<n:
            largest=window[0]
            
            while (-largest[1])<i-k+1:
                heapq.heappop(window)
                largest=window[0]
                # print(largest[1],i-k+1)
            ans.append(-largest[0])
            i+=1
            if i<n:
                heapq.heappush(window,(-nums[i],-i))
            
        return ans
                

