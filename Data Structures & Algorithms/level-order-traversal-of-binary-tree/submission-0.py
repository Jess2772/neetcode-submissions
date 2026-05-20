# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append(root)

        res = []

        while q:
            level = []
            next_level = []
            cur_len = len(q)
            for i in range (cur_len):
                level.append(q[i].val)
                if q[i].left:
                    next_level.append(q[i].left)
                if q[i].right:
                    next_level.append(q[i].right)
            q = next_level[:]
            res.append(level)

        return res
        

                




