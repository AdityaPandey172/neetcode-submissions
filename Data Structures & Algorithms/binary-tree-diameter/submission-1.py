# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node):
            if not node:
                return -1
            nonlocal best

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            best = max(best, left_h + right_h + 2)

            return 1 + max(left_h, right_h)

        dfs(root)
        return best

