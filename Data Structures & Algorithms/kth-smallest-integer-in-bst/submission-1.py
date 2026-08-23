# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.res = 0
        self.count = 0

        def dfs(root, k):
            if not root:
                return None

            dfs(root.left, k)

            self.count += 1
            if self.count == k:
                self.res = root.val
        
            dfs(root.right, k)
        
        dfs(root, k)
        return self.res
            



        