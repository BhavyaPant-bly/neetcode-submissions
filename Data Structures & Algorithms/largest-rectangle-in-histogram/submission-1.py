class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area=0
        stack=[]

        for i in range(0,len(heights)):
            while len(stack) and heights[stack[-1]]>heights[i]:
                length=heights[stack[-1]]
                stack.pop()
                idx = -1 if len(stack)==0 else stack[-1]
                width=i-idx-1
                area=length*width
                largest_area=max(largest_area,area)
            stack.append(i)
        while len(stack):
            length=heights[stack[-1]]
            stack.pop()
            idx=-1 if len(stack)==0 else stack[-1]
            width=len(heights)-idx-1
            largest_area=max(largest_area,length*width)
            
        return largest_area

