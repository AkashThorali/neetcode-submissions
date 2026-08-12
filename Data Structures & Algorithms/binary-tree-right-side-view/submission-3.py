# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        res = []
        stack = deque([root])
        while stack:
            res.append(stack[-1].val)
            for i in range(len(stack)):
                element = stack.popleft()
                if element.left:
                    stack.append(element.left)
                if element.right:
                    stack.append(element.right)
        return res
                
                    


        
                

            

            

        