# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # Diameter through this node = left height + right height
            current_diameter = left_h + right_h
            if current_diameter > self.max_diameter:
                self.max_diameter = current_diameter

            # Return height of this subtree
            return 1 + max(left_h, right_h)

        height(root)
        return self.max_diameter
