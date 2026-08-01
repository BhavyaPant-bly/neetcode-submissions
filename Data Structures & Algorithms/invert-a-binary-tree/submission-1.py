# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue=deque([root])

        while queue:
            temp=queue.popleft()
            temp.left, temp.right=temp.right, temp.left

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return root
