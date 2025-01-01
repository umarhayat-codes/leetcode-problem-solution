# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        queue = [root]

        while queue:
            node = queue.pop(0)
            
            if node and node.val == subRoot.val and self.checkSame(node,subRoot):
                return True 

            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False

    def checkSame(self,root,subRoot):
        if not root or not subRoot:
            return root == subRoot
        
        return root.val == subRoot.val and self.checkSame(root.left,subRoot.left) and self.checkSame(root.right,subRoot.right) 
