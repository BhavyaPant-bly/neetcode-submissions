class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area=0
        while left < right:
            area = min(heights[left],heights[right])*(right-left)
            x=heights[left]
            y=heights[right]
            if x<y:
                left+=1
            elif y<x:
                right-=1
            else:
                left+=1
                right-=1
            if max_area < area:
                max_area = area
        return max_area
        