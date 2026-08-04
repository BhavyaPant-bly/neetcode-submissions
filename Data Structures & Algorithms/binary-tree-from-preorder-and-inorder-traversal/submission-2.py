# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,pre: List[int],inord: List[int], l:int, r:int, x:int)-> Optional[TreeNode]:
        if l>=r or x>=len(pre):
            return None
        ind1=-1
        ind2=-1
        for i in range(x,len(pre)):
            for j in range(l,r):
                if pre[i]==inord[j]:
                    ind1=j
                    ind2=i
                    break
            if ind1 != -1:
                break
        if ind1 ==-1:
            return None

        head=TreeNode(inorder[ind1],None,None)   
        head.left=self.helper(pre,inord,l,ind1,ind2+1) 
        head.right=self.helper(pre,inord,ind1+1,r,ind2+1)

        return head
       


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        return self.helper(preorder,inorder,0,len(inorder),0)
        