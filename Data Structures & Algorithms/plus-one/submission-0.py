class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1

        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1
            c=digits[i]//10
            if c==0:
                return digits
            digits[i]=digits[i]%10
        if c>0:
            new_arr=[c]
            for num in digits:
                new_arr.append(num)
            return new_arr
        return digits
        