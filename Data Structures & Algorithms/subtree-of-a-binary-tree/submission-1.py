# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def same(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        NULL = object()

        def merkle(node, memo):
            if not node:
                return hash(NULL)
            if node in memo:
                return memo[node]
            memo[node] = hash((node.val, merkle(node.left, memo), merkle(node.right, memo)))
            return memo[node]

        target_memo = {}
        target_hash = merkle(subRoot, target_memo)

        memo = {}
        merkle(root, memo)  # fill memo for all nodes in root

        def dfs(node):
            if not node:
                return False
            if memo[node] == target_hash and same(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        