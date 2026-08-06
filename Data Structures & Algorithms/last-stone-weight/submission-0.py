class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heap=stones
        heapq.heapify(heap) 
        while len(heap)>1:
            x=heapq.heappop(heap)  
            y=heapq.heappop(heap)
            if x==y:
                continue
            if x<y:
                heapq.heappush(heap,x-y) 
        return -heap[0] if len(heap) else 0
        