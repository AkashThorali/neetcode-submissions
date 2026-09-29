# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minimum, maximum):
            if not root: 
                return True
            
            if root.val <= minimum or root.val >= maximum: 
                return False
    
            left = dfs(root.left, minimum, root.val)
            right = dfs(root.right, root.val, maximum)
            return left and right

        return dfs(root, float('-inf'), float('inf'))

        