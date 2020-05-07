# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x==root.val or y==root.val:
            return False
        arr=[[root.val]]
        arr1=[[root.val]]
        queue=[root]
        while(1):
            q1=[]
            q2=[]
            q3=[]
            if(len(queue)==0):
                break
            while(1):
                if(len(queue)==0):
                    queue=q1
                    if len(q3)>0:
                        arr1.append(q3)
                    if len(q2)>0:
                        arr.append(q2)
                    break
                x1=queue.pop(0)
                if x1.left is None and x1.right is None:
                    continue
                else:
                    s=[]
                    if x1.left is not None:
                        s.append(x1.left.val)
                        q1.append(x1.left)
                        q3.append(x1.left.val)
                    if x1.right is not None:
                        s.append(x1.right.val)
                        q1.append(x1.right)
                        q3.append(x1.right.val)
                    q2.append(s)
        flag=0
        #print(arr1,arr)
        for i in range(len(arr1)):
            #print(arr1[i])
            if x in arr1[i] and y in arr1[i]:
                flag=i
                #print("harsha")
                break
        if flag==0:
            return False
        else:
            ans=0
            d=arr[flag]
            #print(d)
            for i in range(len(d)):
                if x in d[i] and y in d[i]:
                    ans=1
                    break
            if ans==1:
                return False
            return True
