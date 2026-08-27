class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        squares = [ (x[0]*x[0]+x[1]*x[1]) for x in points]
        heap=[]
        n=len(points)

        for i in range(0,n):
            heap.append((squares[i],points[i]))
        heapq.heapify(heap)
        ans=[]
        for i in range(0,k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        