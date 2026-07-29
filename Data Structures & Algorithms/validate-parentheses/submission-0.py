class Solution:
    def isValid(self, s: str) -> bool:
        brackets={"{":"}","[":"]","(":")"}
        arr=[]
        for c in s:
            if c=="{" or c == "[" or c == "(":
                arr.append(c)
            else:
                if len(arr)==0:
                    return False
                if c != brackets[arr[-1]]:
                    return False
                arr.pop()
        return len(arr)==0
        