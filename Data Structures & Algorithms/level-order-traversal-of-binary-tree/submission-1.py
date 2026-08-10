# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        res = []
        stack = deque([root])
        while stack: 
            temp = []
            for i in range(len(stack)):
                element = stack.popleft()
                if element.left:
                    stack.append(element.left)
                if element.right:
                    stack.append(element.right)
                temp.append(element.val)
            res.append(temp)
        return res
                

        