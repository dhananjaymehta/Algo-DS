"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        self.helper(root)

    def helper(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.helper(node.left)
        self.helper(node.right)