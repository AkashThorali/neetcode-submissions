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

        def in_order_traversal(root, k):
            if not root: 
                return 0

            in_order_traversal(root.left, k)
            
            self.count += 1
            if self.count == k:
                self.res = root.val
            
            in_order_traversal(root.right, k)
            
        in_order_traversal(root, k)
        return self.res


        