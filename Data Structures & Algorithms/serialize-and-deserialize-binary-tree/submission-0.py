# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return "None,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)    
        
        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build_tree(values):
            if values[0] == "None":
                values.pop(0)
                return None

            root = TreeNode(int(values.pop(0)))
            root.left = build_tree(values)
            root.right = build_tree(values)

            return root
        
        values = data.split(",")
        return build_tree(values[:-1])
