class Solution:
    def evaluate(self,a:int,b:int,val:chr):
        if val=="+":
            b=b+a
        elif val == "-":
            b=b-a
        elif val == "*":
            b=b*a
        else:
            b=int(b/a)
        return b

    def evalRPN(self, tokens: List[str]) -> int:

        arr=[]

        exps=['+','-','*','/']

        for val in tokens:
            if val not in exps:
                arr.append(val)
            else:
                a=int(arr[-1])
                b=int(arr[-2])
                arr.pop()
                arr.pop()
                ans=self.evaluate(a,b,val)
                arr.append(str(ans))
        return int(arr[-1])
        