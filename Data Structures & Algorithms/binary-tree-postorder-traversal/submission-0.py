# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        prev = None

        while stack:
            cur = stack[-1]

            if prev is None or prev.left is cur or prev.right is cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
                else:
                    res.append(cur.val)
                    stack.pop()

            elif cur.left is prev:
                if cur.right:
                    stack.append(cur.right)
                else:
                    res.append(cur.val)
                    stack.pop()

            else:
                res.append(cur.val)
                stack.pop()

            prev = cur

        return res        