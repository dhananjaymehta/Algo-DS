"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        return self.helper(root, 0)

    def helper(self, root, h):
        if root is None:
            return h
        h += 1
        return max(self.helper(root.left, h), self.helper(root.right, h))
