# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Returns height if balanced, else returns -1
        def check(node):
            if not node:
                return 0   # height of empty tree

            left = check(node.left)
            if left == -1:
                return -1

            right = check(node.right)
            if right == -1:
                return -1

            # If difference > 1 → not balanced
            if abs(left - right) > 1:
                return -1

            # Return height of subtree
            return max(left, right) + 1

        # If check returns -1, not balanced
        return check(root) != -1
