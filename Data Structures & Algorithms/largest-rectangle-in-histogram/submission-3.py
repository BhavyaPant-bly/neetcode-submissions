# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         largest_area=0
#         stack=[]
#         n=len(heights)
#         i=0
#         while i<n or len(stack):
#             while len(stack) and ((i<n and heights[stack[-1]]>heights[i]) or i==n):
#                 length=heights[stack.pop()]
#                 width=i if len(stack)==0 else i-stack[-1]-1
#                 largest_area=max(largest_area,length*width)
#             if i<n:
#                 stack.append(i)
#             i+=1
            
#         return largest_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Sentinel to flush the stack at the end
        stack = []
        largest_area = 0
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                length = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                largest_area = max(largest_area, length * width)
            stack.append(i)
            
        return largest_area

