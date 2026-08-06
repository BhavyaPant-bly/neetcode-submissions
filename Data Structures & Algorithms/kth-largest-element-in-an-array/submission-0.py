class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        n=len(nums)

        for i in range(0,n):
            if i<k:
                heapq.heappush(heap,nums[i])
            else:
                heapq.heappush(heap,nums[i])
                heapq.heappop(heap)      
        return heap[0]
        