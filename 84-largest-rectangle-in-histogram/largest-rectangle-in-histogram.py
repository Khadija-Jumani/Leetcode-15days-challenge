class Solution:
    def largestRectangleArea(self, heights):
        stack = []             # store indices of increasing bars
        max_area = 0
        # use a sentinel 0 at the end to flush remaining bars from the stack
        heights = heights + [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = height * width
                if area > max_area:
                    max_area = area
            stack.append(i)

        return max_area
