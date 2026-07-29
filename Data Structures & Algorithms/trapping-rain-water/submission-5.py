class Solution:
    def trap(self,height: list[int]) -> int:
        if  len(height)<=2:
            return 0
            
        left_max=0
        right_max=0
        n=len(height)
        water=0
        while right_max < n:
            while left_max < n-1 and height[left_max]<=height[left_max+1]:
                left_max+=1
            right_max=left_max+2
            if right_max >= n:
                break
            while right_max<n and height[right_max-1]>=height[right_max]:
                right_max+=1
            if right_max >= n:
                break
            r=right_max
            while r<n and height[right_max]<=height[left_max]:
                if height[r]>=height[right_max]:
                    right_max=r
                r+=1
            width=right_max-left_max-1
            ht=min(height[right_max],height[left_max])
            water+=width*ht

            print(height[left_max],height[right_max])

            while left_max<right_max-1:
                left_max+=1
                water-=min(ht,height[left_max])
            if r>=n:
                break
            left_max=right_max
        
        return water


                    
