# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=[]
        if root == None:
            return ans
        queue=deque()
        queue.append(root)
        # ans.append(root.val)
        count=1
        
        while queue:
            node=queue.popleft()
            if node.left:
                if node.left.val>=node.val:
                    # ans.append(node.left.val)
                    count+=1
                else:
                    node.left.val=node.val
                queue.append(node.left)
            if node.right:
                if node.right.val>=node.val:
                    # ans.append(node.right.val)
                    count+=1
                else:
                    node.right.val=node.val
                queue.append(node.right)
        # return len(ans)
        return count
        