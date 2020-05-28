# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(root,node):
            if root.val < node: 
                if root.right is None: 
                    root.right = TreeNode(node) 
                else: 
                    build(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = TreeNode(node) 
                else: 
                    build(root.left, node) 
        root=TreeNode(preorder[0])
        print(root.val)
        for i in range(1,len(preorder)):
            build(root,(preorder[i]))
        return root
