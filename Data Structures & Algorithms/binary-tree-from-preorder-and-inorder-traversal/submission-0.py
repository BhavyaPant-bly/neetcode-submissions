# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None
        ind=-1
        for i in preorder:
            if i in inorder:
                ind=inorder.index(i)
                break
        if ind==-1:
            return None
        head=TreeNode(inorder[ind],None,None)
        head.left=self.buildTree(preorder,inorder[:ind])
        head.right=self.buildTree(preorder,inorder[ind+1:])

        return head



        