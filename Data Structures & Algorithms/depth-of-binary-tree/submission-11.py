# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        count = 1
        res = [[root, 1]]
        while res: 
            node, depth = res.pop()
            if node.left:
                res.append([node.left, depth + 1])
            if node.right:
                res.append([node.right, depth + 1])
            count = max(count, depth)
        return count

        

        




        