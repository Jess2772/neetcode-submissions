# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, [-math.inf, math.inf])
    def dfs(self, root, range):
        if not root:
            return True

        if root.val > range[0] and root.val < range[1]:
            return self.dfs(root.left, [range[0], root.val]) and self.dfs(root.right, [root.val, range[1]])
        else:
            return False

        