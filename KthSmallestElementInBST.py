# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
  
        ksmall = -9999999999 # store the Kth smallest  
        curr = root # to store the current node  

        while curr != None: 
            if curr.left == None: 
                count += 1
                if count == k:  
                    ksmall = curr.val
                curr = curr.right 
            else:  
                pre = curr.left  
                while (pre.right != None and pre.right != curr):  
                    pre = pre.right  
                if pre.right == None:  
                    pre.right = curr  
                    curr = curr.left 
                else:  
                    pre.right = None
                    count += 1 
                    if count == k: 
                        ksmall = curr.val  
                    curr = curr.right 
        return ksmall
