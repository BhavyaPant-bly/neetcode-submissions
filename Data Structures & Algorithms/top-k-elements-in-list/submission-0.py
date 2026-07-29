class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct = {}
        for num in nums:
            if num in distinct:
                distinct[num]+=1
            else:
                distinct[num]=1
        distinct = dict(sorted(distinct.items(),key=lambda item : item[1], reverse=True))
        return list(distinct.keys())[:k]

        