class Solution:
    def calc_hrs(self,mid:int, piles: List[int]):
        hrs=0

        for i in piles:
            hrs+=(i//mid)+(1 if i%mid else 0)
        return hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)

        ans=-1

        while start <= end:
            mid = (start+end) // 2
            hrs=self.calc_hrs(mid,piles)
            print(h,hrs)

            if hrs <= h:
                end =mid-1
            else:
                start = mid+1
        return start

