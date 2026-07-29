class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1
        b=nums2
        if len(a)>len(b):
            a,b=b,a
        l=0
        r=len(a)
        half=(len(a)+len(b)+1)//2
        while True:
            mid=(l+r)//2
            aleft=a[mid-1] if mid > 0 else float("-inf")
            aright=a[mid] if mid< len(a) else float("inf")
            bleft=b[half-mid-1] if half-mid > 0 else float("-inf")
            bright=b[half-mid] if half-mid < len(b) else float("inf")

            if aleft<= bright and bleft<= aright:
                if (len(a)+len(b))%2==1:
                    return float(max(aleft,bleft))
                return (max(aleft,bleft)+min(aright,bright))/2.0
            
            if aleft > bright:
                r=mid-1
            else:
                l=mid+1
        return -1.0