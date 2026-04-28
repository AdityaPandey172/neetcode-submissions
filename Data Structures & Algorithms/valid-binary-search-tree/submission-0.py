# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node, prev):
            if not node:
                return True

            if not inorder_traversal(node.left, prev):
                return False
            
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val

            return inorder_traversal(node.right, prev)
        
        prev = [None]
        return inorder_traversal(root, prev)

        