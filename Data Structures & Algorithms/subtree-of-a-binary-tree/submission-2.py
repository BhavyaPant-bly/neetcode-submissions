# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1=deque()
        queue2=deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 or queue2:
            if not queue1 or not queue2:
                return False
            node1=queue1.popleft()
            node2=queue2.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            
            queue1.append(node1.left),queue1.append(node1.right)
            queue2.append(node2.left),queue2.append(node2.right)
        return True
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            if subroot:
                return False
            else:
                return True
        
        if not subRoot:
            return True
        
        queue=deque()
        queue.append(root)

        while queue:
            node=queue.popleft()
            if node.val == subRoot.val:
                result=self.isSameTree(node,subRoot)
                if result:
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False

        
        