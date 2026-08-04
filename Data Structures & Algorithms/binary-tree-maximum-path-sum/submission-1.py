# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.maxSum=-1001
    def helper(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return -1001
        res1=self.helper(root.left)
        res2=self.helper(root.right)
        y=-1001
        if res1 == -1001 and res2 == -1001:
            y=root.val
        elif res2 == -1001:
            y=max(root.val,root.val+res1)
        elif res1 == -1001:
            y=max(root.val,root.val+res2)
        else:
            y=max(root.val,root.val+res1,root.val+res2)
            self.maxSum=max(y,root.val+res1+res2,self.maxSum)
        self.maxSum=max(self.maxSum,y)
        return y
        

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxSum

        