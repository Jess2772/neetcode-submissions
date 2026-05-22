# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder[0] is the root of the tree:
        # you can look for preorder[0] in the inorder array. 
        #    that elements to the left are in the left subtree
        #    elements to the right are in the right subtree
        # preorder[1] would be the left child of the root 
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])

        midIndex = inorder.index(root.val)
        leftInorder = inorder[:midIndex]
        rightInorder = inorder[midIndex + 1:]
 
        leftPreorder = preorder[1:1 + len(leftInorder)]
        rightPreorder = preorder[1 + len(leftInorder):]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root




        