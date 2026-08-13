class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0

        # holds a pair of values (index, height)
        stack = [] 

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])

        for i in stack: 
            maxArea = max(maxArea, i[1] * (len(heights) - i[0]))
        return maxArea

        