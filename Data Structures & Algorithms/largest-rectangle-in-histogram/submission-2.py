class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area=0
        stack=[]
        n=len(heights)
        i=0
        while i<n or len(stack):
            while len(stack) and ((i<n and heights[stack[-1]]>heights[i]) or i==n):
                length=heights[stack[-1]]
                stack.pop()
                idx = -1 if len(stack)==0 else stack[-1]
                width=i-idx-1
                area=length*width
                largest_area=max(largest_area,area)
            if i<n:
                stack.append(i)
            i+=1
            
        return largest_area

