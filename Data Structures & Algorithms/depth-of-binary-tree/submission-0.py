# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth=0
        queue=deque()
        queue.append(root)
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            if queue[0]==None:
                queue.popleft()
                depth+=1
                if len(queue):
                    queue.append(None)
        return depth

        